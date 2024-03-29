import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments
import torch

# Load Dataset
df = pd.read_csv("C:/Users/allwy/Documents/GitHub/demand-forecasting/demand-forecasting-backend/data/Historical Product Demand.csv")
df = df.sample(frac=0.1).reset_index(drop=True) # shuffle dataframe

# Preprocess the Data
df["text_data"] = "The demand for " + df["Product_Code"] + " from " + df["Warehouse"] + " belonging to " + df["Product_Category"] + " on " + df["Date"] + " was " + df["Order_Demand"].apply(str)

# Convert dataframe to text file
df["text_data"].to_frame().to_csv('text_data.txt', index=False, header=False)

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Load pretrained model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Enable gradient checkpointing to save memory
model.config.gradient_checkpointing = True

# Load dataset
train_dataset = TextDataset(
          tokenizer=tokenizer,
          file_path="text_data.txt",
          block_size=128)

# Define data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False)

# Initialize our Trainer
training_args = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=4,  # Reduce the batch size
    save_steps=1000,  # Save after every 1000 steps
    save_total_limit=2,
    prediction_loss_only=True,
    fp16=True, # Enable fp16 for less memory usage
    gradient_accumulation_steps=2, # Gradient accumulation
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Training
trainer.train()

# Save the Fine-Tuned Model
trainer.save_model("fine_tuned_gpt2")  # Save model directly from the trainer
torch.save(model.state_dict(), 'fine_tuned_gpt2.pth')  # Save model state dict