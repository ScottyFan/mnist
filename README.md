# MNIST Docker Project

Docker deployment of PyTorch MNIST training.

## Files
- `Dockerfile` - Container configuration
- `main.py` - PyTorch MNIST training script
- `requirements.txt` - Dependencies
- `README.md` -  Description
- `Report` -  Compare the results with analysis

## Quick Start
Create a GCP project

Enable billing

Enable APIs: Container, Compute, Artifact Registry

## Local GCP CLI Setup
gcloud auth login

gcloud config set project wfgpuchase

gcloud services enable container.googleapis.com compute.googleapis.com

## Build Docker Image
docker build -t mnist-pytorch .

## Test Docker Run Locally 
docker run mnist-pytorch

## Push to Google Container Registry
docker tag mnist-pytorch gcr.io/wfgpuchase/mnist-pytorch:latest

gcloud auth configure-docker

docker push gcr.io/wfgpuchase/mnist-pytorch:latest

## Deploy with Terraform
terraform init

terraform apply -var="project_id=wfgpuchase"

## Run
gcloud container clusters get-credentials 

mnist-training-cluster --region us-central1

kubectl create job mnist-training --image=gcr.io/wfgpuchase/mnist-pytorch:latest

kubectl logs -f job/mnist-training


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


# Screen Output

![alt text](/screen_output/auth.png)
![alt text](/screen_output/gcloud.png)
![alt text](/screen_output/pytorch.png)
![alt text](/screen_output/tag.png)