import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from torch.utils.data import Dataset

# Step 1: Load the Dataset
df = pd.read_csv("C:/Users/allwy/Documents/GitHub/demand-forecasting/demand-forecasting-backend/data/Historical Product Demand.csv")

# Step 2: Preprocess the Data
# Concatenate relevant columns into a single text format
df["text_data"] = df["Product_Code"] + " " + df["Warehouse"] + " " + df["Product_Category"] + " " + df["Date"]

# Drop rows with missing values in the "text_data" column
df = df.dropna(subset=["text_data"])

# Step 3: Tokenize the Data
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
df["tokenized_text"] = df["text_data"].apply(lambda x: tokenizer.encode(x, add_special_tokens=True))

# Step 4: Define Dataset Class
class DemandForecastDataset(Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]

# Step 5: Fine-Tune the Model
model = GPT2LMHeadModel.from_pretrained("gpt2")
dataset = DemandForecastDataset(df["tokenized_text"].tolist())

training_args = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=8,
    save_steps=1000,
    save_total_limit=2,
    logging_dir="./logs",
    logging_steps=100,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer,
)

trainer.train()

# Step 6: Evaluate the Model (Optional)
trainer.evaluate()

# Step 7: Save the Fine-Tuned Model
model.save_pretrained("fine_tuned_demand_forecast_model")
tokenizer.save_pretrained("fine_tuned_demand_forecast_tokenizer")
