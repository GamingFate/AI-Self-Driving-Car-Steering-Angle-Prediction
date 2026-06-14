import pandas as pd
import numpy as np
import os
import cv2
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Lambda, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import Sequence
import tensorflow as tf
import matplotlib.pyplot as plt

# GPU memory growth
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

# ─────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────
MODEL_OUT  = r"F:\major project 8th sem\Self Driving Car\Mboth1_2_3rd.h5"

IMG_HEIGHT = 66
IMG_WIDTH  = 200
IMG_CH     = 3
BATCH_SIZE = 32
EPOCHS     = 25

# ─────────────────────────────────────────
# LOAD + COMBINE DATASETS
# ─────────────────────────────────────────
print("Loading datasets...")

columns = ['center', 'left', 'right', 'steering', 'throttle', 'brake', 'speed']

df1 = pd.read_csv(
    r"F:\major project 8th sem\Self Driving Car\track 1 dataset\driving_log.csv",
    header=None
)
df1.columns = columns

df2 = pd.read_csv(
    r"F:\major project 8th sem\Self Driving Car\track 2 dataset\driving_log.csv",
    header=None
)
df2.columns = columns

df = pd.concat([df1, df2], ignore_index=True)

# keep only required columns
df = df[['center', 'steering']]

# convert steering to float
df['steering'] = df['steering'].astype(float)

print(f"Total combined samples: {len(df)}")

# ─────────────────────────────────────────
# BALANCE DATASET
# ─────────────────────────────────────────
print("Balancing dataset...")

straight = df[df['steering'] == 0]
turning  = df[df['steering'] != 0]

max_straight = min(len(straight), len(turning) * 2)

straight = straight.sample(max_straight, random_state=42)

df = pd.concat([straight, turning])
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

print(f"Total samples after balancing: {len(df)}")
print(f"Straight: {(df['steering']==0).sum()} | Turning: {(df['steering']!=0).sum()}")

# ─────────────────────────────────────────
# TRAIN / VALIDATION SPLIT
# ─────────────────────────────────────────
train_df, val_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

print(f"Train: {len(train_df)} | Val: {len(val_df)}")

# ─────────────────────────────────────────
# DATA GENERATOR
# ─────────────────────────────────────────
class DataGenerator(Sequence):

    def __init__(self, dataframe, batch_size, img_h, img_w, augment=False):
        self.df = dataframe.reset_index(drop=True)
        self.batch_size = batch_size
        self.img_h = img_h
        self.img_w = img_w
        self.augment = augment

    def __len__(self):
        return int(np.ceil(len(self.df) / self.batch_size))

    def __getitem__(self, idx):

        batch = self.df.iloc[
            idx * self.batch_size:(idx + 1) * self.batch_size
        ]

        X, y = [], []

        for _, row in batch.iterrows():

            full_path = row['center'].strip()

            # check file exists
            if not os.path.exists(full_path):
                continue

            # read image
            img = cv2.imread(full_path)

            if img is None:
                continue

            # resize image
            img = cv2.resize(img, (self.img_w, self.img_h))

            # convert BGR to YUV
            img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

            # convert datatype
            img = img.astype(np.float32)

            steering_val = row['steering']

            # horizontal flip augmentation
            if self.augment and np.random.rand() < 0.5:
                img = cv2.flip(img, 1)
                steering_val = -steering_val

            X.append(img)
            y.append(steering_val)

        # safety fallback
        if len(X) == 0:
            return np.zeros((1, self.img_h, self.img_w, 3)), np.zeros((1,))

        return np.array(X), np.array(y, dtype=np.float32)

    def on_epoch_end(self):
        self.df = self.df.sample(frac=1).reset_index(drop=True)

# training generator
train_gen = DataGenerator(
    train_df,
    BATCH_SIZE,
    IMG_HEIGHT,
    IMG_WIDTH,
    augment=True
)

# validation generator
val_gen = DataGenerator(
    val_df,
    BATCH_SIZE,
    IMG_HEIGHT,
    IMG_WIDTH,
    augment=False
)

# ─────────────────────────────────────────
# NVIDIA CNN MODEL
# ─────────────────────────────────────────
model = Sequential([

    Lambda(
        lambda x: x / 127.5 - 1.0,
        input_shape=(IMG_HEIGHT, IMG_WIDTH, IMG_CH)
    ),

    Conv2D(24, (5, 5), strides=(2, 2), activation='relu'),
    Conv2D(36, (5, 5), strides=(2, 2), activation='relu'),
    Conv2D(48, (5, 5), strides=(2, 2), activation='relu'),

    Conv2D(64, (3, 3), activation='relu'),
    Conv2D(64, (3, 3), activation='relu'),

    Flatten(),

    Dropout(0.5),

    Dense(100, activation='relu'),
    Dense(50, activation='relu'),
    Dense(10, activation='relu'),

    Dense(1)
])

model.summary()

# ─────────────────────────────────────────
# COMPILE MODEL
# ─────────────────────────────────────────
model.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss='mse'
)

# ─────────────────────────────────────────
# TRAIN MODEL
# ─────────────────────────────────────────
print("\nTraining started...")

history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS
)

# ─────────────────────────────────────────
# SAVE MODEL
# ─────────────────────────────────────────
model.save(MODEL_OUT)

print(f"\n✅ Model saved to: {MODEL_OUT}")

# ─────────────────────────────────────────
# PLOT LOSS CURVE
# ─────────────────────────────────────────
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')

plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('MSE Loss')

plt.legend()

plt.savefig(
    r"F:\major project 8th sem\Self Driving Car\loss_plot_both.png"
)

plt.show()

print("Loss plot saved.")