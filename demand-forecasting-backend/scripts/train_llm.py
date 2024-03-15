import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

# Load Dataset
df = pd.read_csv("C:/Users/allwy/Documents/GitHub/demand-forecasting/demand-forecasting-backend/data/Historical Product Demand.csv")
df = df.sample(frac=0.1).reset_index(drop=True) # shuffle dataframe

# Preprocess the Data
df["text_data"] = "The demand for " + df["Product_Code"] + " from " + df["Warehouse"] + " belonging to " + df["Product_Category"] + " on " + df["Date"] + " was " + df["Order_Demand"].apply(str)

# Convert dataframe to text file
df["text_data"].to_frame().to_csv('text_data.txt', index=False, header=False)

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2', gradient_checkpointing = True) # enable gradient checkpointing to save memory

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
    save_steps=10_000,
    save_total_limit=2,
    prediction_loss_only=True,
    fp16=True, # Enable fp16 for less memory usage
    gradient_accumulation_steps=2 # Gradient accumulation
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

trainer.train()

# Save the Fine-Tuned Model
model.save_pretrained("fine_tuned_gpt2")
