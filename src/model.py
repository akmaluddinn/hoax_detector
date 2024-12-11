import torch
from transformers import BertTokenizer, BertForSequenceClassification
import streamlit as st

@st.cache(allow_output_mutation=True)
def load_model(model_path='model/model.pth'):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    tokenizer = BertTokenizer.from_pretrained('indobenchmark/indobert-base-p1')
    model = BertForSequenceClassification.from_pretrained('indobenchmark/indobert-base-p1', num_labels=2)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    return model, tokenizer, device

def predict(model, text, tokenizer, device, max_len=128):
    model.eval()
    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=max_len,
        padding='max_length',
        return_attention_mask=True,
        truncation=True,
        return_tensors='pt',
    )
    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)
    
    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=1).item()
    
    return "Berita Palsu" if prediction == 1 else "Berita Asli"
