# cog-parakeet-rnnt-1.1b
nvidia/parakeet-rnnt-1.1b running in Replicate Cog container ⚙️

[![Replicate](https://replicate.com/nvlabs/parakeet-rnnt-1.1b/badge)](https://replicate.com/nvlabs/parakeet-rnnt-1.1b)

# Parakeet RNNT 1.1B 🦜

*Tweet by Vaibhav (VB) Srivastav (@reach_vb): "Parakeet RNNT & CTC models top the Open ASR Leaderboard! With @NVIDIAAI and @suno_ai_, parakeet surpasses Whisper, reclaiming the top spot."*

---

## Model Description 📝
The Parakeet RNNT 1.1B, crafted by NVIDIA and Suno.ai, is an advanced ASR model excelling in transcribing English speech with high accuracy. It features the FastConformer architecture and is available in RNNT and CTC versions, suited for noisy audio environments and maintaining accuracy in silent segments.

For more details, visit the model's page on Hugging Face: [Parakeet RNNT 1.1B on Hugging Face](https://huggingface.co/nvidia/parakeet-rnnt-1.1b)

## Benchmark Comparison 📊
The 🤗 [Open ASR Leaderboard on Hugging Face](https://huggingface.co/spaces/asr/leaderboard) that ranks speech recognition models. It uses two main metrics for evaluation: Average Word Error Rate (WER) and Real-Time Factor (RTF), where _lower is better_. These metrics help in understanding a model's accuracy and efficiency in processing speech.

| Model                  | Average WER | RTF (1e-3) | AMI | Earnings22 | Gigaspeech | LS Clean | LS Other | SPGISpeech | Tedlium | Voxpopuli | Common Voice 9 |
|------------------------|-----------------|----------------|-----|------------|------------|----------|----------|------------|---------|-----------|----------------|
| [nvidia/parakeet-rnnt-1.1b](https://huggingface.co/nvidia/parakeet-rnnt-1.1b) | 7.04            | 14.4           | 17.1 | 14.15      | 9.96      | 1.46     | 2.48     | 3.11      | 3.92    | 5.39      | 5.8            |
| [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3)   | 7.7             | 7.45           | 16.01 | 11.3       | 10.02     | 2.03     | 3.91     | 2.95      | 3.9     | 9.52      | 9.67           |

## Intended Use 🎯
This model is designed for precise ASR tasks in voice recognition and transcription, effective in varied audio backgrounds. It's compatible with the NeMo toolkit for a range of uses.

## Ethical Considerations 🤔
Users should be mindful of data privacy and the potential for biases in speech recognition, ensuring fair and responsible use of the technology.

## Caveats and Recommendations ⚠️
Optimized for 16,000 Hz mono-channel audio, the model outputs in lower-case English. Its training on a 65K-hour diverse dataset indicates robust performance, but testing in specific use cases is recommended.

## Licence 📜
Parakeet RNNT 1.1B is licensed under CC-BY-4.0, permitting both personal and commercial usage with proper attribution.
