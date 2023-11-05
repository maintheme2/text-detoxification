# Baseline

As a baseline model, the T5-base model was used. T5 (Text-to-Text Transfer Transformer) is a versatile and powerful NLP model that can be fine-tuned for various text-related tasks, including text detoxification. The T5 model is an encoder-decoder, known for its excellence in capturing contextual information in text data. The T5-base model was fine-tuned on the paranmt dataset for text detoxification purposes.

# Hypothesis 1: Changing the hyperparameters

I tried different **batch sizes**, especially when I tried to train my model endlessly, because every time it crashed due to lack of computing power. To free up the GPU a bit, I set the evaluation batch size to 4. I also set **eval_accumulation_steps** to move the predictions to the CPU to free up the GPU memory faster. This increased the training time drastically.

# Results
As a result, my model's performance was pretty good, there were quite nice evaluation scores.