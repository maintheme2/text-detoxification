import warnings
warnings.filterwarnings("ignore")
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Seq2SeqTrainingArguments, Seq2SeqTrainer

print('Loading tokenizer...')
tokenizer = AutoTokenizer.from_pretrained('t5-base', local_files_only = True)
print('Loading model...')
model = AutoModelForSeq2SeqLM.from_pretrained('../../models/t5-base', local_files_only = True)

print('Please input your text: ')
reference = input()
# check if reference is a string
if type(reference) != str:
    print('Please input a string')
    reference = input()

tokenized_ref = tokenizer(reference, return_tensors = "pt")

translation = model.generate(input_ids = tokenized_ref["input_ids"], attention_mask = tokenized_ref["attention_mask"], max_length = 128, num_return_sequences = 1)
preds = [tokenizer.decode(gen_id, skip_special_tokens = True, clean_up_tokenization_spaces=True)
        for gen_id in translation]

print(preds[0])