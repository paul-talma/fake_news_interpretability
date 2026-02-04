# pipeline spec

- load dataset
    - place dataset into memory
- sample k from dataset
    - selects k data points from the dataset
    - k should be a variable parameter
    - should be able to select whether the sampling is random or from the first k
    - random sampling should be seeded
- make prompts
    - prompts should be structured as follows:
        - system: "You are a news trustworthiness classifier.\n"
          "Your task is to classify news articles as either trustworthy or untrustworthy.\n"
          "Your answer should consist of exactly one token: 0 if the article is untrustworthy and 1 if it is trustworthy.\n\n"
        - user: "ARTICLE: {article}\n\n"
          "CLASSIFICATION (0 or 1):"

- load model
    - this should be modular, to make it easy to switch between models
    - default model should be "Qwen/Qwen2.5-0.5B-Instruct"
- load tokenizer
    - the tokenizer should have a variable context length
- run model
    - this runs the model on the k loaded samples, collecting model outputs
- extract classifications
    - this should extract a classification from the model output (a simple regex or _ is in _ should suffice)
- compute metrics
    - simple classification metrics (accuracy)
- display graphs
    - this should take in the metrics corresponding to different models and display them on a common chart

