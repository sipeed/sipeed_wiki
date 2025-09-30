# Deploying AI Models on M4C

## Deploying Large Language and Multimodal Models

Obtain models and runtime environments from the following sources. Deployment instructions can be found in each repository's README.md.

Official AXERA Models: https://huggingface.co/AXERA-TECH

China Mirror Site: https://hf-mirror.com/AXERA-TECH

| Model | Link | China Mirror Link |
|  --  |  --  |  --  |
| Qwen3:0.6b | [Qwen3-0.6B-Int8](https://huggingface.co/AXERA-TECH/Qwen3-0.6B)  | [Qwen3-0.6B-Int8](https://hf-mirror.com/AXERA-TECH/Qwen3-0.6B) |
| DeepSeek-R1:1.5b | [DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/AXERA-TECH/DeepSeek-R1-Distill-Qwen-1.5B)  | [DeepSeek-R1-Distill-Qwen-1.5B](https://hf-mirror.com/AXERA-TECH/DeepSeek-R1-Distill-Qwen-1.5B) |
| Qwen2.5:1.5b | [Qwen2.5-1.5B-Instruct-GPTQ-Int8](https://huggingface.co/AXERA-TECH/Qwen2.5-1.5B-Instruct-GPTQ-Int8)  | [Qwen2.5-1.5B-Instruct-GPTQ-Int8](https://hf-mirror.com/AXERA-TECH/Qwen2.5-1.5B-Instruct-GPTQ-Int8) |
| SD1.5 | [lcm-lora-sdv1-5](https://huggingface.co/AXERA-TECH/lcm-lora-sdv1-5)  | [lcm-lora-sdv1-5](https://hf-mirror.com/AXERA-TECH/lcm-lora-sdv1-5) |
| InternVL2.5:1b | [InternVL2_5-1B-Int8](https://huggingface.co/AXERA-TECH/InternVL2_5-1B)  | [InternVL2_5-1B-Int8](https://hf-mirror.com/AXERA-TECH/InternVL2_5-1B) |

**Important Note:** All above models require system images compiled with `SDK 1.45.0` or `later` to run large models. Please update your system accordingly. Our provided TFCard&eMMC images meet this requirement and reserve 6GB memory for model loading, capable of running 7B parameter int4 models.

*Quick test with Qwen3-0.6b:*
```bash
# Can replace with links to other model repositories
git clone https://hf-mirror.com/AXERA-TECH/Qwen3-0.6B

cd Qwen3-0.6B

# If ModuleNotFoundError occurs, refer to FAQ for details
python3 qwen3_tokenizer_uid.py

# Switch to corresponding execution script and restore necessary permissions
chmod +x main_ax650
sh run_qwen3_0.6b_int8_ctx_ax650.sh
```
