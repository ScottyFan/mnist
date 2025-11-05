# MNIST Docker Project

Simple Docker deployment of PyTorch MNIST training with hyperparameter experiments.

## Files
- `Dockerfile` - Container configuration (MODIFIED: custom CMD with epochs=5, batch-size=128, lr=0.5)
- `main.py` - PyTorch MNIST training script
- `requirements.txt` - Dependencies (torch, torchvision, matplotlib)
- `README.md` - This file

## Quick Start

### 1. Build Docker Image
```bash
docker build -t mnist-pytorch .
```

### 2. Run with Default Parameters (from Dockerfile CMD)
```bash
docker run --name mnist-run mnist-pytorch 2>&1 | tee docker-run.out
docker rm mnist-run
```

### 3. Run Experiments with Different Hyperparameters

**Experiment 1: Baseline (5 epochs, batch 64, lr 1.0)**
```bash
docker run mnist-pytorch python main.py --epochs 5 --batch-size 64 --lr 1.0 2>&1 | tee exp1.log
```

**Experiment 2: Large Batch (5 epochs, batch 256, lr 1.0)**
```bash
docker run mnist-pytorch python main.py --epochs 5 --batch-size 256 --lr 1.0 2>&1 | tee exp2.log
```

**Experiment 3: More Epochs (10 epochs, batch 64, lr 1.0)**
```bash
docker run mnist-pytorch python main.py --epochs 10 --batch-size 64 --lr 1.0 2>&1 | tee exp3.log
```

**Experiment 4: Lower Learning Rate (5 epochs, batch 64, lr 0.5)**
```bash
docker run mnist-pytorch python main.py --epochs 5 --batch-size 64 --lr 0.5 2>&1 | tee exp4.log
```

## Available Parameters

- `--epochs` - Number of training epochs (default: 14)
- `--batch-size` - Training batch size (default: 64)
- `--lr` - Learning rate (default: 1.0)
- `--gamma` - Learning rate decay (default: 0.7)
- `--log-interval` - Logging frequency (default: 10)
- `--save-model` - Save trained model
- `--dry-run` - Quick test

## Analyzing Results

Each experiment log shows:
- Training loss per epoch
- Test accuracy after each epoch
- Final accuracy (typically 95-99%)

Compare the logs to see effects of:
- **Batch Size**: Larger = faster training but may reduce accuracy
- **Epochs**: More = better accuracy up to a point
- **Learning Rate**: Higher = faster convergence but less stable

## Key Modifications

### Dockerfile Changes:
1. **Custom CMD line** with default hyperparameters (epochs=5, batch-size=128, lr=0.5)
   - Original: Would need manual parameter specification every run
   - Benefit: Container runs immediately with sensible defaults

## Container Benefits

- **Reproducibility**: Same results on any system
- **Isolation**: No dependency conflicts with host
- **Portability**: Easy to share and deploy
- **Consistency**: Identical environment every time

## Expected Results

- Training time: ~2-3 minutes per 5 epochs (CPU)
- Final accuracy: 95-99% on MNIST
- Larger batches train faster but may need LR adjustment
- More epochs improve accuracy but have diminishing returns

## Troubleshooting

**Docker daemon not running:**
```bash
sudo systemctl start docker
```

**Out of memory:**
```bash
docker run mnist-pytorch python main.py --batch-size 32
```

**Interactive mode for debugging:**
```bash
docker run -it mnist-pytorch bash
```