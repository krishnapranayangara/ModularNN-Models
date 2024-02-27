# Modular Deep learning models

Modularity in Deep learning Models have become imperative due to the rapid growth in research and in the number of SOTA models being developed that are resource intensive and time consuming.

#### Pipeline

![image](https://github.com/krishnapranayangara/modulardlmodels/assets/33367492/70d6a8e9-d3b0-4fed-a55c-fd0c68deb238)

#### Methodology

![image](https://github.com/krishnapranayangara/modulardlmodels/assets/33367492/2ab7d0a9-59e9-4c77-b60d-f8a5b4fd93a7)

In order to understand the effects of compression, we have taken two SOTA models (Alexnet and ZFNet) and tried to compress them using three different techniques.
For the compression techniques, we have considered,
- Post training quantization
- Quantization Aware Training
- Knowledge distillation

**For each of these two models, I have worked on these three compression techniques and tested them to understand their effects on accuracy and precision.

- First technique, Post training quantization is a way of quantizing an already trained model.
- Second technique, Quantization aware training is a technique of being conscious about memory consumption during the model's training process.
- Third technique Knowledge distillation is the process of transferring knowledge from a large model to a smaller one. In this case, larger models are Alexnet and ZFNet and smaller models are our own models.
- The primary metrics on which we have evaluated these models are accuracy, time and model size.

