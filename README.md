# 🏥 MLOps Diabetes Prediction - End-to-End Production Pipeline

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5.svg)](https://kubernetes.io/)
[![AWS](https://img.shields.io/badge/AWS-EKS-FF9900.svg)](https://aws.amazon.com/eks/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **A complete, production-ready MLOps project demonstrating industry best practices for deploying machine learning models at scale using Kubernetes, Docker, and AWS infrastructure. Follow this guide to build the exact same project step-by-step!**

**🌐 Live Demo**: [https://mlops.abhimishra-devops.com](https://mlops.abhimishra-devops.com)  
**📚 API Documentation**: [https://mlops.abhimishra-devops.com/docs](https://mlops.abhimishra-devops.com/docs)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [What You'll Learn](#-what-youll-learn)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Complete Setup Guide](#-complete-setup-guide)
  - [Phase 1: Local Development](#phase-1-local-development-setup)
  - [Phase 2: Containerization](#phase-2-containerization)
  - [Phase 3: Local Kubernetes](#phase-3-local-kubernetes-deployment)
  - [Phase 4: AWS Setup](#phase-4-aws-infrastructure-setup)
  - [Phase 5: Production Deployment](#phase-5-production-deployment-on-eks)
  - [Phase 6: Domain & HTTPS](#phase-6-domain--https-configuration)
- [Troubleshooting](#-troubleshooting)
- [Common Commands Cheat Sheet](#-common-commands-cheat-sheet)
- [Project Structure](#-project-structure)
- [API Usage Examples](#-api-usage-examples)
- [Cost Estimation](#-cost-estimation)
- [Next Steps](#-next-steps)

---

## 🎯 Overview

This project implements a **complete end-to-end MLOps pipeline** for predicting diabetes risk using machine learning. It's designed as a **learning resource** and **portfolio project** that demonstrates real-world DevOps and MLOps practices.

### What Makes This Project Special?

✅ **Beginner-Friendly**: Step-by-step instructions with explanations  
✅ **Production-Ready**: Real AWS infrastructure, not just localhost  
✅ **Complete Pipeline**: From model training to HTTPS deployment  
✅ **Cost-Effective**: Uses free-tier eligible resources where possible  
✅ **Resume-Worthy**: Demonstrates multiple in-demand skills  

---

## 📚 What You'll Learn

By following this guide, you'll gain hands-on experience with:

| Category | Skills |
|----------|--------|
| **Machine Learning** | Model training, evaluation, scikit-learn, feature engineering |
| **API Development** | FastAPI, RESTful APIs, async programming, data validation |
| **Containerization** | Docker, multi-stage builds, image optimization, ECR |
| **Kubernetes** | Pods, Deployments, Services, Ingress, scaling, health checks |
| **Cloud Infrastructure** | AWS EKS, VPC, IAM, security groups, networking |
| **DevOps** | CI/CD concepts, GitOps, infrastructure as code |
| **Networking** | DNS (Route 53), load balancing (ALB), SSL/TLS (ACM) |
| **Security** | HTTPS, IAM roles, secrets management, least privilege |

---

## ✨ Key Features

### 🧠 Machine Learning
- **Diabetes prediction model** trained on Pima Indians dataset
- **RESTful API** for real-time predictions
- **Model persistence** with pickle
- **Feature validation** and error handling

### 🐳 Containerization
- **Multi-stage Docker builds** for optimized image size
- **AWS ECR integration** for private Docker registry
- **Health checks** and logging
- **Environment configuration**

### ☸️ Kubernetes Orchestration
- **Local development** with Kind cluster
- **Production deployment** on AWS EKS
- **Auto-scaling** with Horizontal Pod Autoscaler
- **Rolling updates** and zero-downtime deployments
- **Service discovery** and load balancing

### ☁️ AWS Cloud Infrastructure
- **EKS (Elastic Kubernetes Service)** - Managed Kubernetes
- **ECR (Elastic Container Registry)** - Private Docker registry
- **Route 53** - DNS management and routing
- **ACM (AWS Certificate Manager)** - Free SSL certificates
- **IAM** - Secure access control with IRSA
- **ALB (Application Load Balancer)** - Layer 7 load balancing
- **VPC** - Isolated network environment

### 🔒 Security & Best Practices
- **HTTPS-only** communication
- **IAM Roles for Service Accounts** (IRSA)
- **Network policies** and security groups
- **Secrets management** with Kubernetes
- **Least privilege** access control

---

## 🏗️ Architecture

```
                          ┌─────────────────────┐
                          │   Internet Users    │
                          └──────────┬──────────┘
                                     │
                                     ▼
                          ┌─────────────────────┐
                          │     Route 53        │
                          │  DNS Resolution     │
                          │  mlops.abhimishra-  │
                          │  devops.com → ALB   │
                          └──────────┬──────────┘
                                     │
                                     ▼
                ┌────────────────────────────────────────┐
                │   AWS Application Load Balancer        │
                │   - SSL/TLS Termination (ACM Cert)     │
                │   - Health Checks                      │
                │   - Traffic Distribution               │
                └───────────────┬────────────────────────┘
                                │
                                ▼
                ┌────────────────────────────────────────┐
                │     Kubernetes Ingress Resource        │
                │  (AWS Load Balancer Controller)        │
                │  - Routing Rules                       │
                │  - Path-based Routing                  │
                └───────────────┬────────────────────────┘
                                │
                                ▼
                ┌────────────────────────────────────────┐
                │     Kubernetes Service (ClusterIP)     │
                │  - Internal Load Balancing             │
                │  - Service Discovery                   │
                └───────────────┬────────────────────────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
                ▼               ▼               ▼
        ┌───────────┐   ┌───────────┐   ┌───────────┐
        │   Pod 1   │   │   Pod 2   │   │   Pod 3   │
        ├───────────┤   ├───────────┤   ├───────────┤
        │  FastAPI  │   │  FastAPI  │   │  FastAPI  │
        │    App    │   │    App    │   │    App    │
        │           │   │           │   │           │
        │ ML Model  │   │ ML Model  │   │ ML Model  │
        └───────────┘   └───────────┘   └───────────┘
                │
                └──────────────┬──────────────────────┐
                               │                      │
                               ▼                      ▼
                    ┌─────────────────┐    ┌─────────────────┐
                    │   AWS ECR       │    │   AWS EKS       │
                    │ Docker Registry │    │ Control Plane   │
                    └─────────────────┘    └─────────────────┘
```

### Data Flow:
1. **User Request** → HTTPS request to custom domain
2. **DNS Resolution** → Route 53 resolves to ALB DNS
3. **Load Balancer** → ALB terminates SSL, forwards to Ingress
4. **Ingress Controller** → Routes request to appropriate Service
5. **Service** → Load balances across healthy Pods
6. **Pod** → FastAPI processes request, ML model predicts
7. **Response** → Returns JSON prediction through same path

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Python 3.9+ | ML model and API development |
| **ML Libraries** | scikit-learn, pandas, numpy | Model training and data processing |
| **API Framework** | FastAPI, Uvicorn | REST API and async server |
| **Containerization** | Docker | Application packaging |
| **Container Registry** | AWS ECR | Private Docker image storage |
| **Orchestration** | Kubernetes (Kind, EKS) | Container orchestration |
| **Package Manager** | Helm 3 | Kubernetes application management |
| **Cloud Provider** | AWS | Infrastructure and services |
| **Compute** | EKS (Managed K8s) | Kubernetes cluster management |
| **Load Balancing** | AWS ALB | Application load balancing |
| **DNS** | Route 53 | Domain name management |
| **SSL/TLS** | ACM | Free SSL certificates |
| **IAM** | AWS IAM | Identity and access management |
| **Networking** | AWS VPC | Network isolation |
| **CLI Tools** | AWS CLI, eksctl, kubectl | Infrastructure management |
| **Version Control** | Git, GitHub | Source code management |

---

## 📦 Prerequisites

### Required Software (Install Before Starting)

#### 1. **Python 3.9+**
```bash
# Check version
python3 --version

# If not installed:
# macOS: brew install python@3.9
# Ubuntu: sudo apt install python3.9 python3.9-venv python3-pip
# Windows: Download from python.org
```

#### 2. **Docker Desktop**
```bash
# Check version
docker --version
docker-compose --version

# Install from: https://www.docker.com/products/docker-desktop
# Minimum version: Docker 20.10+
```

#### 3. **kubectl (Kubernetes CLI)**
```bash
# Check version
kubectl version --client

# Install:
# macOS: brew install kubectl
# Linux: curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
# Windows: choco install kubernetes-cli
```

#### 4. **Kind (Kubernetes in Docker)**
```bash
# Check version
kind version

# Install:
# macOS: brew install kind
# Linux: curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
# Windows: choco install kind
```

#### 5. **Helm (Kubernetes Package Manager)**
```bash
# Check version
helm version

# Install:
# macOS: brew install helm
# Linux: curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
# Windows: choco install kubernetes-helm
```

#### 6. **AWS CLI v2**
```bash
# Check version
aws --version

# Install from: https://aws.amazon.com/cli/
# Minimum version: 2.0+
```

#### 7. **eksctl (EKS CLI)**
```bash
# Check version
eksctl version

# Install:
# macOS: brew install eksctl
# Linux: curl --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp && sudo mv /tmp/eksctl /usr/local/bin
# Windows: choco install eksctl
```

### AWS Account Requirements

1. **Active AWS Account** - [Sign up here](https://aws.amazon.com/free/)
2. **AWS CLI Configured** - With your credentials
3. **IAM Permissions** - Ensure your user has:
   - EKS full access
   - ECR full access
   - Route 53 full access
   - ACM full access
   - IAM role creation
   - VPC and EC2 permissions

### Optional (For Custom Domain)
- **Domain Name** - Purchase from Route 53 or any registrar
- **Route 53 Hosted Zone** - If using external registrar

---

## 🚀 Complete Setup Guide

Follow these phases in order. Each phase builds on the previous one.

---

## **Phase 1: Local Development Setup**

### Step 1.1: Clone the Repository
```bash
# Clone the project
git clone https://github.com/Abhi-mishra998/mlops-diabetes-prediction-aws.git

# Navigate to project directory
cd mlops-diabetes-prediction-aws

# Check contents
ls -la
```

**Expected Output:**
```
deployment.yaml
Dockerfile
download_dataset.sh
ingress.yaml
k8s-deploy.yml
main.py
requirements.txt
service.yaml
train.py
```

### Step 1.2: Create Python Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Your prompt should now show (venv)
```

### Step 1.3: Install Python Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Verify installation
pip list
```

**Key Packages:**
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `scikit-learn` - ML library
- `pandas` - Data manipulation
- `numpy` - Numerical computing

### Step 1.4: Download Dataset
```bash
# Make script executable
chmod +x download_dataset.sh

# Run download script
bash download_dataset.sh

# Verify dataset exists
ls -lh diabetes.csv
```

**Note:** If download fails, manually download from [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) and place in project root.

### Step 1.5: Train the ML Model
```bash
# Run training script
python train.py
```

**Expected Output:**
```
Loading dataset...
Dataset shape: (768, 9)
Training model...
Model trained successfully!
Accuracy: 0.77
Model saved to: models/diabetes_model.pkl
```

**What Happened:**
- Loaded diabetes dataset
- Split into train/test sets
- Trained Logistic Regression model
- Evaluated on test set
- Saved model to `models/` directory

### Step 1.6: Test API Locally
```bash
# Start FastAPI server
python main.py
```

**Expected Output:**
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**In a new terminal**, test the API:

```bash
# Test health endpoint
curl http://localhost:8000/health

# Expected: {"status":"healthy","model":"loaded"}

# Test prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "features": [6, 148, 72, 35, 0, 33.6, 0.627, 50]
  }'

# Expected: {"prediction":1,"probability":0.85,"risk_level":"high"}
```

**Visit in Browser:**
- API Docs: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

✅ **Phase 1 Complete!** Your ML model is working locally.

---

## **Phase 2: Containerization**

### Step 2.1: Review Dockerfile
```bash
# View Dockerfile contents
cat Dockerfile
```

**Dockerfile Explanation:**
```dockerfile
FROM python:3.9-slim          # Base image
WORKDIR /app                  # Working directory
COPY requirements.txt .       # Copy dependencies
RUN pip install --no-cache-dir -r requirements.txt  # Install
COPY . .                      # Copy application code
EXPOSE 8000                   # Expose port
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]  # Run
```

### Step 2.2: Build Docker Image
```bash
# Build image with tag
docker build -t mlops-diabetes-model:latest .

# Verify image created
docker images | grep mlops-diabetes

# Check image size
docker images mlops-diabetes-model:latest --format "{{.Size}}"
```

**Expected Output:**
```
REPOSITORY              TAG       IMAGE ID       CREATED         SIZE
mlops-diabetes-model    latest    abc123def456   10 seconds ago  450MB
```

### Step 2.3: Run Docker Container
```bash
# Run container in detached mode
docker run -d \
  --name diabetes-api \
  -p 8000:8000 \
  mlops-diabetes-model:latest

# Check container is running
docker ps

# View container logs
docker logs diabetes-api

# Follow logs in real-time
docker logs -f diabetes-api
```

### Step 2.4: Test Containerized API
```bash
# Test health check
curl http://localhost:8000/health

# Test prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [6, 148, 72, 35, 0, 33.6, 0.627, 50]}'

# Open browser to: http://localhost:8000/docs
```

### Step 2.5: Container Management Commands
```bash
# Stop container
docker stop diabetes-api

# Start container
docker start diabetes-api

# Remove container
docker rm -f diabetes-api

# View all containers (including stopped)
docker ps -a

# Clean up unused images
docker image prune -a
```

✅ **Phase 2 Complete!** Your application is containerized.

---

## **Phase 3: Local Kubernetes Deployment**

### Step 3.1: Create Kind Cluster
```bash
# Create cluster named mlops-local
kind create cluster --name mlops-local

# Verify cluster created
kind get clusters

# Check kubectl context
kubectl config current-context

# Should show: kind-mlops-local
```

### Step 3.2: Load Docker Image to Kind
```bash
# Load your Docker image into Kind cluster
kind load docker-image mlops-diabetes-model:latest --name mlops-local

# Verify image loaded
docker exec -it mlops-local-control-plane crictl images | grep mlops
```

**Why:** Kind runs Kubernetes in Docker, so we need to load our image into the Kind cluster's local registry.

### Step 3.3: Review Kubernetes Manifests

**deployment.yaml** - Defines how to run your app:
```bash
cat deployment.yaml
```

Key sections:
- `replicas: 3` - Run 3 pods
- `image:` - Your Docker image
- `resources:` - CPU/memory limits
- `livenessProbe:` - Health check endpoint
- `readinessProbe:` - Ready check endpoint

**service.yaml** - Exposes your app internally:
```bash
cat service.yaml
```

Key sections:
- `type: ClusterIP` - Internal service (or LoadBalancer for cloud)
- `port: 80` - External port
- `targetPort: 8000` - Container port
- `selector:` - Matches deployment labels

**ingress.yaml** - Routes external traffic:
```bash
cat ingress.yaml
```

Key sections:
- `host:` - Domain name
- `path:` - URL path
- `backend:` - Service to route to

### Step 3.4: Deploy to Kind Cluster
```bash
# Apply deployment
kubectl apply -f deployment.yaml

# Wait for deployment to be ready
kubectl wait --for=condition=available --timeout=300s deployment/diabetes-deployment

# Apply service
kubectl apply -f service.yaml

# Apply ingress (optional for Kind)
kubectl apply -f ingress.yaml
```

### Step 3.5: Verify Deployment
```bash
# Check all resources
kubectl get all

# Check pods in detail
kubectl get pods -o wide

# Check pod logs
kubectl logs -l app=diabetes-api

# Describe deployment
kubectl describe deployment diabetes-deployment

# Check service
kubectl get svc diabetes-service
```

**Expected Pod Status:**
```
NAME                                   READY   STATUS    RESTARTS   AGE
diabetes-deployment-xxxx-yyyy          1/1     Running   0          2m
diabetes-deployment-xxxx-zzzz          1/1     Running   0          2m
diabetes-deployment-xxxx-wwww          1/1     Running   0          2m
```

### Step 3.6: Access Application via Port Forward
```bash
# Forward local port to service
kubectl port-forward service/diabetes-service 8000:80

# In new terminal, test
curl http://localhost:8000/health

# Test prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [6, 148, 72, 35, 0, 33.6, 0.627, 50]}'
```

### Step 3.7: Kubernetes Debugging Commands
```bash
# View pod logs
kubectl logs -f deployment/diabetes-deployment

# Execute command in pod
kubectl exec -it deployment/diabetes-deployment -- /bin/bash

# Inside pod, test locally
curl http://localhost:8000/health
exit

# View events
kubectl get events --sort-by='.lastTimestamp'

# Describe pod for issues
kubectl describe pod <pod-name>
```

### Step 3.8: Clean Up Kind (Optional)
```bash
# Delete resources
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
kubectl delete -f ingress.yaml

# Delete cluster
kind delete cluster --name mlops-local
```

✅ **Phase 3 Complete!** Your app runs on Kubernetes locally.

---

## **Phase 4: AWS Infrastructure Setup**

### Step 4.1: Configure AWS CLI
```bash
# Configure AWS credentials
aws configure

# You'll be prompted for:
# AWS Access Key ID: [Your Access Key]
# AWS Secret Access Key: [Your Secret Key]
# Default region name: ap-south-1
# Default output format: json

# Test configuration
aws sts get-caller-identity
```

**Expected Output:**
```json
{
    "UserId": "AIDAI...",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/your-name"
}
```

**Save your Account ID** - you'll need it later:
```bash
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
echo $AWS_ACCOUNT_ID
```

### Step 4.2: Set Environment Variables
```bash
# Set project variables
export CLUSTER_NAME=mlops-cluster
export REGION=ap-south-1
export NODE_TYPE=t3.medium
export NODES=2

# Verify variables
echo "Cluster: $CLUSTER_NAME"
echo "Region: $REGION"
echo "Node Type: $NODE_TYPE"
echo "Nodes: $NODES"
echo "Account: $AWS_ACCOUNT_ID"
```

**Save these to a file** for future use:
```bash
cat > aws-env.sh << 'EOF'
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
export CLUSTER_NAME=mlops-cluster
export REGION=ap-south-1
export NODE_TYPE=t3.medium
export NODES=2
EOF

# Source it anytime
source aws-env.sh
```

### Step 4.3: Create EKS Cluster
```bash
# Create EKS cluster (takes 15-20 minutes)
eksctl create cluster \
  --name $CLUSTER_NAME \
  --region $REGION \
  --nodes $NODES \
  --node-type $NODE_TYPE \
  --with-oidc \
  --managed

# This creates:
# - EKS cluster control plane
# - 2 EC2 worker nodes (t3.medium)
# - VPC with subnets
# - Security groups
# - IAM roles
# - OIDC provider
```

**What to Expect:**
- Process takes 15-20 minutes
- You'll see CloudFormation stack creation
- Two stacks: cluster and nodegroup
- Don't interrupt the process

**While Waiting:**
- Grab coffee ☕
- Read about [EKS architecture](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
- Review your `deployment.yaml` file

**After Completion:**
```bash
# Verify cluster
eksctl get cluster --name $CLUSTER_NAME --region $REGION

# Configure kubectl
aws eks update-kubeconfig --name $CLUSTER_NAME --region $REGION

# Test connection
kubectl get nodes

# Check cluster info
kubectl cluster-info
```

**Expected Nodes:**
```
NAME                                          STATUS   ROLES    AGE   VERSION
ip-192-168-x-x.ap-south-1.compute.internal    Ready    <none>   5m    v1.27.x
ip-192-168-y-y.ap-south-1.compute.internal    Ready    <none>   5m    v1.27.x
```

### Step 4.4: Install AWS Load Balancer Controller

**Why:** EKS needs this controller to automatically create and manage AWS Application Load Balancers from Kubernetes Ingress resources.

#### 4.4a: Download IAM Policy
```bash
# Download policy
curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json

# Review policy (optional)
cat iam-policy.json | head -20
```

#### 4.4b: Create IAM Policy
```bash
# Create policy
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam-policy.json

# If policy exists, you'll see error - that's OK!
# Note the ARN in output
```

#### 4.4c: Create IAM Service Account
```bash
# Create service account with IAM role
eksctl create iamserviceaccount \
    --cluster=$CLUSTER_NAME \
    --namespace=kube-system \
    --name=aws-load-balancer-controller \
    --attach-policy-arn=arn:aws:iam::${AWS_ACCOUNT_ID}:policy/AWSLoadBalancerControllerIAMPolicy \
    --approve \
    --region=$REGION

# Verify service account
kubectl get sa -n kube-system aws-load-balancer-controller

# Check IAM role annotation
kubectl describe sa -n kube-system aws-load-balancer-controller
```

#### 4.4d: Install Controller with Helm
```bash
# Install CRDs (Custom Resource Definitions)
kubectl apply -k "github.com/aws/eks-charts/stable/aws-load-balancer-controller//crds?ref=master"

# Add EKS Helm repo
helm repo add eks https://aws.github.io/eks-charts
helm repo update

# Get VPC ID
export VPC_ID=$(aws eks describe-cluster --name $CLUSTER_NAME --region $REGION --query "cluster.resourcesVpcConfig.vpcId" --output text)
echo "VPC ID: $VPC_ID"

# Install controller
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=$CLUSTER_NAME \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set region=$REGION \
  --set vpcId=$VPC_ID

# Verify installation
kubectl get deployment -n kube-system aws-load-balancer-controller

# Check logs
kubectl logs -n kube-system deployment/aws-load-balancer-controller
```

**Expected Output:**
```
NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
aws-load-balancer-controller   2/2     2            2           1m
```

✅ **Phase 4 Complete!** AWS infrastructure is ready.

---

## **Phase 5: Production Deployment on EKS**

### Step 5.1: Create ECR Repository
```bash
# Create private repository
aws ecr create-repository \
    --repository-name mlops-diabetes-model \
    --region $REGION

# Get repository URI
export ECR_URI="${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/mlops-diabetes-model"
echo "ECR URI: $ECR_URI"
```

### Step 5.2: Login to ECR
```bash
# Get login password and authenticate Docker
aws ecr get-login-password --region $REGION | \
    docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

# You should see: "Login Succeeded"
```

### Step 5.3: Tag and Push Docker Image
```bash
# Tag your local image for ECR
docker tag mlops-diabetes-model:latest $ECR_URI:latest

# Also tag with version
docker tag mlops-diabetes-model:latest $ECR_URI:v1.0

# Verify tags
docker images | grep mlops-diabetes

# Push to ECR (this may take a few minutes)
docker push $ECR_URI:latest
docker push $ECR_URI:v1.0

# Verify in ECR
aws ecr describe-images \
    --repository-name mlops-diabetes-model \
    --region $REGION
```

### Step 5.4: Update Deployment Manifest

**Edit `deployment.yaml`** to use ECR image:

```bash
# Backup original
cp deployment.yaml deployment.yaml.backup

# Update image URL (replace with your ECR URI)
sed -i "s|image:.*|image: ${ECR_URI}:latest|g" deployment.yaml

# Verify change
grep "image:" deployment.yaml
```

**Manual Alternative:**
Open `deployment.yaml` and find:
```yaml
spec:
  containers:
  - name: diabetes-api
    image: mlops-diabetes-model:latest  # Change this line
```

Replace with:
```yaml
spec:
  containers:
  - name: diabetes-api
    image: 123456789012.dkr.ecr.ap-south-1.amazonaws.com/mlops-diabetes-model:latest
```

### Step 5.5: Update Service Manifest

**Edit `service.yaml`** for LoadBalancer type:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: diabetes-service
spec:
  type: LoadBalancer  # Change from ClusterIP
  selector:
    app: diabetes-api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
```

### Step 5.6: Deploy to EKS
```bash
# Apply deployment
kubectl apply -f deployment.yaml

# Wait for rollout
kubectl rollout status deployment/diabetes-deployment

# Apply service
kubectl apply -f service.yaml

# Apply ingress
kubectl apply -f ingress.yaml

# Check all resources
kubectl get all
```

### Step 5.7: Verify Pods are Running
```bash
# Check pod status
kubectl get pods -o wide

# Check pod details
kubectl describe pods -l app=diabetes-api

# View logs from all pods
kubectl logs -l app=diabetes-api --tail=50

# Follow logs in real-time
kubectl logs -f deployment/diabetes-deployment

# Check if pods are ready
kubectl get pods -l app=diabetes-api -o jsonpath='{.items[*].status.conditions[?(@.type=="Ready")].status}'
```

**Expected Output:**
```
NAME                                   READY   STATUS    RESTARTS   AGE
diabetes-deployment-xxxxx-yyyyy        1/1     Running   0          2m
diabetes-deployment-xxxxx-zzzzz        1/1     Running   0          2m
diabetes-deployment-xxxxx-wwwww        1/1     Running   0          2m
```

### Step 5.8: Get Load Balancer URL
```bash
# Get service details
kubectl get svc diabetes-service

# Get load balancer hostname (may take 2-3 minutes to provision)
kubectl get svc diabetes-service -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'

# Save to variable
export LB_URL=$(kubectl get svc diabetes-service -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
echo "Load Balancer URL: $LB_URL"
```

**Wait until you see:**
```
NAME               TYPE           CLUSTER-IP       EXTERNAL-IP                              PORT(S)
diabetes-service   LoadBalancer   10.100.123.45    abc123-456.ap-south-1.elb.amazonaws.com  80:32000/TCP
```

### Step 5.9: Test Load Balancer
```bash
# Test health endpoint (might take 1-2 minutes for health checks to pass)
curl http://$LB_URL/health

# Test prediction
curl -X POST http://$LB_URL/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [6, 148, 72, 35, 0, 33.6, 0.627, 50]}'

# Check in browser
echo "Visit: http://$LB_URL/docs"
```

### Step 5.10: Get Ingress Load Balancer
```bash
# Check ingress status
kubectl get ingress

# Get ALB DNS name
kubectl get ingress diabetes-ingress -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'

# Save to variable
export ALB_DNS=$(kubectl get ingress diabetes-ingress -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
echo "ALB DNS: $ALB_DNS"

# Get ALB Hosted Zone ID (needed for Route 53)
export ALB_ZONE=$(aws elbv2 describe-load-balancers \
  --query "LoadBalancers[?DNSName=='$ALB_DNS'].CanonicalHostedZoneId" \
  --output text)
echo "ALB Zone ID: $ALB_ZONE"
```

**Note:** It may take 5-10 minutes for the ALB to be fully provisioned and healthy.

✅ **Phase 5 Complete!** Your app is running on AWS EKS!

---

## **Phase 6: Domain & HTTPS Configuration**

### Step 6.1: Request SSL Certificate from ACM

```bash
# Request certificate for your domain
aws acm request-certificate \
  --domain-name mlops.abhimishra-devops.com \
  --validation-method DNS \
  --region $REGION

# Get certificate ARN
export CERT_ARN=$(aws acm list-certificates \
  --region $REGION \
  --query "CertificateSummaryList[?DomainName=='mlops.abhimishra-devops.com'].CertificateArn" \
  --output text)

echo "Certificate ARN: $CERT_ARN"

# Get validation details
aws acm describe-certificate \
  --certificate-arn $CERT_ARN \
  --region $REGION \
  --query "Certificate.DomainValidationOptions[0].ResourceRecord"
```

**Expected Output:**
```json
{
    "Name": "_abc123xyz.mlops.abhimishra-devops.com.",
    "Type": "CNAME",
    "Value": "_def456uvw.acm-validations.aws."
}
```

**Save these values** - you'll add them to Route 53!

### Step 6.2: Get Hosted Zone ID

```bash
# List all hosted zones
aws route53 list-hosted-zones

# Get specific hosted zone ID
export HOSTED_ZONE_ID=$(aws route53 list-hosted-zones \
  --query "HostedZones[?Name=='abhimishra-devops.com.'].Id" \
  --output text | cut -d'/' -f3)

echo "Hosted Zone ID: $HOSTED_ZONE_ID"
```

**If you don't have a hosted zone:**
```bash
# Create hosted zone for your domain
aws route53 create-hosted-zone \
  --name abhimishra-devops.com \
  --caller-reference $(date +%s)
```

### Step 6.3: Add ACM Validation CNAME to Route 53

**Using the values from Step 6.1:**

```bash
# Get validation CNAME details
export VALIDATION_NAME=$(aws acm describe-certificate \
  --certificate-arn $CERT_ARN \
  --region $REGION \
  --query "Certificate.DomainValidationOptions[0].ResourceRecord.Name" \
  --output text)

export VALIDATION_VALUE=$(aws acm describe-certificate \
  --certificate-arn $CERT_ARN \
  --region $REGION \
  --query "Certificate.DomainValidationOptions[0].ResourceRecord.Value" \
  --output text)

echo "Validation Name: $VALIDATION_NAME"
echo "Validation Value: $VALIDATION_VALUE"

# Add validation record
aws route53 change-resource-record-sets \
    --hosted-zone-id $HOSTED_ZONE_ID \
    --change-batch '{
      "Changes": [{
        "Action": "UPSERT",
        "ResourceRecordSet": {
          "Name": "'$VALIDATION_NAME'",
          "Type": "CNAME",
          "TTL": 300,
          "ResourceRecords": [{"Value": "'$VALIDATION_VALUE'"}]
        }
      }]
    }'
```

### Step 6.4: Wait for Certificate Validation

```bash
# Wait for validation (can take 5-30 minutes)
echo "Waiting for certificate validation..."
aws acm wait certificate-validated \
  --certificate-arn $CERT_ARN \
  --region $REGION

echo "✅ Certificate validated!"

# Verify status
aws acm describe-certificate \
  --certificate-arn $CERT_ARN \
  --region $REGION \
  --query "Certificate.Status"
```

**While waiting**, you can check status:
```bash
# Check validation status
aws acm describe-certificate \
  --certificate-arn $CERT_ARN \
  --region $REGION \
  --query "Certificate.DomainValidationOptions[0].ValidationStatus"
```

**Expected Statuses:**
- `PENDING_VALIDATION` → Waiting
- `SUCCESS` → Validated ✅

### Step 6.5: Update Ingress with SSL Certificate

**Edit `ingress.yaml`** to add HTTPS:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: diabetes-ingress
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    # Add these annotations for HTTPS:
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS": 443}]'
    alb.ingress.kubernetes.io/ssl-redirect: '443'
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:ap-south-1:123456789012:certificate/abc-123-xyz
spec:
  ingressClassName: alb
  rules:
  - host: mlops.abhimishra-devops.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: diabetes-service
            port:
              number: 80
```

**Or use sed to update:**
```bash
# Backup ingress
cp ingress.yaml ingress.yaml.backup

# Add certificate ARN annotation
kubectl annotate ingress diabetes-ingress \
  alb.ingress.kubernetes.io/certificate-arn=$CERT_ARN \
  --overwrite

# Add HTTPS listener
kubectl annotate ingress diabetes-ingress \
  alb.ingress.kubernetes.io/listen-ports='[{"HTTP": 80}, {"HTTPS": 443}]' \
  --overwrite

# Add SSL redirect
kubectl annotate ingress diabetes-ingress \
  alb.ingress.kubernetes.io/ssl-redirect='443' \
  --overwrite
```

**Reapply ingress:**
```bash
kubectl apply -f ingress.yaml

# Wait for ALB to update (2-3 minutes)
kubectl get ingress diabetes-ingress -w
```

### Step 6.6: Create Route 53 A Record for Domain

```bash
# Make sure ALB_DNS and ALB_ZONE are set
echo "ALB DNS: $ALB_DNS"
echo "ALB Zone: $ALB_ZONE"

# If not set, get them again:
export ALB_DNS=$(kubectl get ingress diabetes-ingress -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
export ALB_ZONE=$(aws elbv2 describe-load-balancers \
  --query "LoadBalancers[?DNSName=='$ALB_DNS'].CanonicalHostedZoneId" \
  --output text)

# Create A record pointing to ALB
aws route53 change-resource-record-sets \
    --hosted-zone-id $HOSTED_ZONE_ID \
    --change-batch '{
      "Changes": [{
        "Action": "UPSERT",
        "ResourceRecordSet": {
          "Name": "mlops.abhimishra-devops.com",
          "Type": "A",
          "AliasTarget": {
            "HostedZoneId": "'$ALB_ZONE'",
            "DNSName": "'$ALB_DNS'",
            "EvaluateTargetHealth": false
          }
        }
      }]
    }'
```

**Verify DNS record:**
```bash
# List records
aws route53 list-resource-record-sets \
  --hosted-zone-id $HOSTED_ZONE_ID \
  --query "ResourceRecordSets[?Name=='mlops.abhimishra-devops.com.']"
```

### Step 6.7: Wait for DNS Propagation

```bash
# Check DNS resolution (may take 1-5 minutes)
nslookup mlops.abhimishra-devops.com

# Or use dig
dig mlops.abhimishra-devops.com

# Wait until it resolves to ALB DNS
watch -n 5 'dig mlops.abhimishra-devops.com +short'
```

### Step 6.8: Test HTTPS Endpoint

```bash
# Test health check
curl https://mlops.abhimishra-devops.com/health

# Test prediction
curl -X POST https://mlops.abhimishra-devops.com/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [6, 148, 72, 35, 0, 33.6, 0.627, 50]}'

# Test HTTP redirect to HTTPS
curl -I http://mlops.abhimishra-devops.com/health
# Should return 301 or 302 redirect to HTTPS

# Open in browser
echo "Visit: https://mlops.abhimishra-devops.com/docs"
```

### Step 6.9: Verify SSL Certificate

```bash
# Check certificate details
openssl s_client -connect mlops.abhimishra-devops.com:443 -servername mlops.abhimishra-devops.com < /dev/null

# Check certificate expiry
echo | openssl s_client -servername mlops.abhimishra-devops.com -connect mlops.abhimishra-devops.com:443 2>/dev/null | openssl x509 -noout -dates
```

**Visit in browser:**
- https://mlops.abhimishra-devops.com
- https://mlops.abhimishra-devops.com/docs
- https://mlops.abhimishra-devops.com/redoc

**Check for:**
- 🔒 Padlock icon in address bar
- Valid SSL certificate
- No security warnings

✅ **Phase 6 Complete!** Your app has HTTPS with custom domain!

---

## 🎉 Congratulations!

Your **complete MLOps pipeline** is now live at:
**https://mlops.abhimishra-devops.com**

### What You've Built:

✅ **Machine Learning Model** - Trained and evaluated  
✅ **REST API** - FastAPI with async support  
✅ **Docker Container** - Optimized image  
✅ **Kubernetes Deployment** - Auto-scaling pods  
✅ **AWS EKS Cluster** - Managed Kubernetes  
✅ **Private Docker Registry** - AWS ECR  
✅ **Load Balancing** - AWS ALB with health checks  
✅ **Custom Domain** - Route 53 DNS  
✅ **HTTPS/SSL** - Free ACM certificate  
✅ **Production-Ready** - Secure, scalable infrastructure  

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### **Issue 1: Pods Not Starting**

```bash
# Check pod status
kubectl get pods

# Describe pod for details
kubectl describe pod <pod-name>

# Check logs
kubectl logs <pod-name>

# Common fixes:
# - Image pull error: Check ECR URI in deployment.yaml
# - CrashLoopBackOff: Check application logs
# - ImagePullBackOff: Verify ECR authentication
```

**Solution for Image Pull Errors:**
```bash
# Recreate ECR login
aws ecr get-login-password --region $REGION | \
    docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

# Verify image exists in ECR
aws ecr describe-images --repository-name mlops-diabetes-model --region $REGION
```

#### **Issue 2: Load Balancer Not Created**

```bash
# Check ingress status
kubectl describe ingress diabetes-ingress

# Check load balancer controller logs
kubectl logs -n kube-system deployment/aws-load-balancer-controller

# Common fixes:
# - Check IAM permissions
# - Verify service account
# - Check VPC/subnet tags
```

**Solution:**
```bash
# Verify controller is running
kubectl get deployment -n kube-system aws-load-balancer-controller

# Check service account annotations
kubectl describe sa -n kube-system aws-load-balancer-controller

# Recreate ingress
kubectl delete ingress diabetes-ingress
kubectl apply -f ingress.yaml
```

#### **Issue 3: Certificate Validation Stuck**

```bash
# Check certificate status
aws acm describe-certificate --certificate-arn $CERT_ARN --region $REGION

# Verify CNAME record in Route 53
aws route53 list-resource-record-sets --hosted-zone-id $HOSTED_ZONE_ID

# Common fixes:
# - Check CNAME values match exactly
# - Wait longer (can take 30 minutes)
# - Delete and recreate certificate
```

**Solution:**
```bash
# Delete old certificate
aws acm delete-certificate --certificate-arn $CERT_ARN --region $REGION

# Request new certificate
aws acm request-certificate \
  --domain-name mlops.abhimishra-devops.com \
  --validation-method DNS \
  --region $REGION

# Add validation CNAME again
```

#### **Issue 4: 502 Bad Gateway**

```bash
# Check if pods are running
kubectl get pods

# Check if pods are ready
kubectl get pods -o jsonpath='{.items[*].status.conditions[?(@.type=="Ready")].status}'

# Check target group health
aws elbv2 describe-target-health --target-group-arn <target-group-arn>

# Common fixes:
# - Pods not passing health checks
# - Wrong port in service
# - Security group blocking traffic
```

**Solution:**
```bash
# Check pod health
kubectl exec -it <pod-name> -- curl http://localhost:8000/health

# Verify service endpoints
kubectl get endpoints diabetes-service

# Check if ALB can reach pods
kubectl logs -l app=diabetes-api --tail=50
```

#### **Issue 5: DNS Not Resolving**

```bash
# Check A record exists
aws route53 list-resource-record-sets \
  --hosted-zone-id $HOSTED_ZONE_ID \
  --query "ResourceRecordSets[?Name=='mlops.abhimishra-devops.com.']"

# Test DNS resolution
nslookup mlops.abhimishra-devops.com
dig mlops.abhimishra-devops.com

# Common fixes:
# - Wait for DNS propagation (up to 48 hours, usually 5 minutes)
# - Check nameservers match registrar
# - Verify A record points to correct ALB
```

#### **Issue 6: HTTPS Not Working**

```bash
# Check certificate is attached to ALB
kubectl describe ingress diabetes-ingress | grep certificate-arn

# Test SSL
curl -vI https://mlops.abhimishra-devops.com

# Common fixes:
# - Certificate not validated
# - Wrong certificate ARN in ingress
# - Listener not configured for HTTPS
```

#### **Issue 7: High Costs**

```bash
# Check running resources
eksctl get cluster --name $CLUSTER_NAME --region $REGION
kubectl get nodes

# Stop cluster when not needed
eksctl scale nodegroup --cluster=$CLUSTER_NAME --nodes=0 --name=<nodegroup-name>

# Delete cluster completely
eksctl delete cluster --name $CLUSTER_NAME --region $REGION
```

---

## 📝 Common Commands Cheat Sheet

### **Git Commands**
```bash
git status                          # Check repo status
git add .                           # Stage all changes
git commit -m "message"             # Commit changes
git push origin main                # Push to GitHub
git pull origin main                # Pull latest changes
git log --oneline                   # View commit history
```

### **Docker Commands**
```bash
docker build -t <name> .            # Build image
docker images                       # List images
docker ps                           # List running containers
docker ps -a                        # List all containers
docker run -p 8000:8000 <image>     # Run container
docker stop <container-id>          # Stop container
docker rm <container-id>            # Remove container
docker logs <container-id>          # View logs
docker exec -it <container-id> bash # Enter container
docker system prune -a              # Clean up everything
```

### **Kubernetes Commands**
```bash
# Viewing Resources
kubectl get all                     # All resources
kubectl get pods                    # List pods
kubectl get svc                     # List services
kubectl get ingress                 # List ingresses
kubectl get nodes                   # List nodes
kubectl get events                  # View events

# Describing Resources
kubectl describe pod <pod-name>     # Pod details
kubectl describe svc <svc-name>     # Service details
kubectl describe ingress <ing-name> # Ingress details

# Logs and Debugging
kubectl logs <pod-name>             # View logs
kubectl logs -f <pod-name>          # Follow logs
kubectl logs -l app=<label>         # Logs by label
kubectl exec -it <pod-name> -- bash # Enter pod

# Applying Manifests
kubectl apply -f <file.yaml>        # Apply config
kubectl delete -f <file.yaml>       # Delete config
kubectl replace -f <file.yaml>      # Replace config

# Port Forwarding
kubectl port-forward svc/<service> 8000:80  # Forward port

# Scaling
kubectl scale deployment <name> --replicas=5  # Scale deployment

# Rolling Updates
kubectl set image deployment/<name> container=image:tag  # Update image
kubectl rollout status deployment/<name>                 # Check status
kubectl rollout undo deployment/<name>                   # Rollback
```

### **AWS CLI Commands**
```bash
# General
aws configure                       # Configure credentials
aws sts get-caller-identity         # Check credentials
aws eks list-clusters               # List EKS clusters

# EKS
aws eks update-kubeconfig --name <cluster> --region <region>  # Configure kubectl
aws eks describe-cluster --name <cluster>                     # Cluster details

# ECR
aws ecr get-login-password --region <region>                  # Get login password
aws ecr describe-repositories                                 # List repositories
aws ecr describe-images --repository-name <repo>              # List images

# Route 53
aws route53 list-hosted-zones                                 # List zones
aws route53 list-resource-record-sets --hosted-zone-id <id>   # List records

# ACM
aws acm list-certificates --region <region>                   # List certificates
aws acm describe-certificate --certificate-arn <arn>          # Cert details

# Load Balancers
aws elbv2 describe-load-balancers                             # List ALBs
aws elbv2 describe-target-groups                              # List target groups
```

### **eksctl Commands**
```bash
eksctl create cluster --name <name> --region <region>     # Create cluster
eksctl get cluster                                         # List clusters
eksctl get nodegroup --cluster <name>                      # List node groups
eksctl scale nodegroup --cluster <name> --nodes <count>    # Scale nodes
eksctl delete cluster --name <name>                        # Delete cluster
```

### **Helm Commands**
```bash
helm repo add <name> <url>          # Add repository
helm repo update                    # Update repos
helm search repo <keyword>          # Search charts
helm install <name> <chart>         # Install chart
helm list                           # List releases
helm uninstall <name>               # Uninstall release
helm upgrade <name> <chart>         # Upgrade release
```

---

## 📂 Project Structure

```
mlops-diabetes-prediction-aws/
│
├── README.md                       # This comprehensive guide
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies
├── aws-env.sh                      # AWS environment variables
│
├── train.py                        # ML model training script
├── main.py                         # FastAPI application
├── download_dataset.sh             # Dataset download script
│
├── Dockerfile                      # Docker build instructions
│
├── deployment.yaml                 # Kubernetes Deployment
├── service.yaml                    # Kubernetes Service
├── ingress.yaml                    # Kubernetes Ingress
├── k8s-deploy.yml                  # Alternative K8s config
│
├── iam-policy.json                 # ALB Controller IAM policy
│
├── models/                         # ML model artifacts (gitignored)
│   └── diabetes_model.pkl          # Trained model
│
├── venv/                           # Python virtual environment (gitignored)
│
└── .git/                           # Git repository


⭐ If you find this project helpful, please give it a star!

```
### **Author**
Abhishek-Mishra
```
