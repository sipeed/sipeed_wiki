---
title: K3s 部署
---

## 简介
[K3s](https://k3s.io/) 是轻量级的 Kubernetes。它易于安装，仅需要 Kubernetes 内存的一半，适用于资源有限的环境，特别是边缘计算、物联网等应用场景。

## 部署教程

### 准备环境
首先，确保集群的网络正常，并且能够访问互联网。你可以使用 SSH 远程登录到集群中的每台机器，执行后续安装命令。确保主节点和工作节点的 IP 地址固定，并且网络间能够互相访问。

###  安装 K3s（主节点）
K3s 的安装非常简单。你只需在主节点上运行以下命令：
``` bash
curl -sfL https://get.k3s.io | sh -
```
如果下载很慢可以使用以下命令加速安装
``` bash
curl -sfL https://rancher-mirror.rancher.cn/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn sh -
```
该命令会自动下载并安装 K3s。安装过程完成后，通过以下命令检查 K3s 服务是否启动：
``` bash
sudo systemctl status k3s
```
如果显示 `active (running)`，表示 K3s 已成功启动。

```bash
sudo systemctl status k3s
● k3s.service - Lightweight Kubernetes
     Loaded: loaded (/etc/systemd/system/k3s.service; enabled; preset: enabled)
     Active: active (running) since Mon 2025-02-17 12:07:15 CST; 3h 38min ago
       Docs: https://k3s.io
    Process: 8803 ExecStartPre=/bin/sh -xc ! /usr/bin/systemctl is-enabled --quiet nm-cloud-setup.service 2>/dev/null (code=exited, status=0/SUCCESS)
    Process: 8805 ExecStartPre=/sbin/modprobe br_netfilter (code=exited, status=0/SUCCESS)
    Process: 8808 ExecStartPre=/sbin/modprobe overlay (code=exited, status=0/SUCCESS)
   Main PID: 8810 (k3s-server)
      Tasks: 32
     Memory: 583.2M
        CPU: 29min 49.755s
     CGroup: /system.slice/k3s.service
             ├─8810 "/usr/local/bin/k3s server"
             └─8895 "containerd "
```

### 安装 K3s（工作节点）
在工作节点上安装 K3s 时，需要将工作节点与主节点连接。使用以下命令在工作节点上安装 K3s：
``` bash
curl -sfL https://get.k3s.io | K3S_URL=https://<主节点IP>:6443 K3S_TOKEN=<主节点Token> sh -
```
上述命令中，`主节点IP` 需要替换为主节点的 IP 地址，`主节点Token` 是从主节点获取的令牌。你可以通过以下命令在主节点上查看令牌：
```bash
sudo cat /var/lib/rancher/k3s/server/node-token
```
安装完成后，使用以下命令验证工作节点是否成功加入集群：
```bash
sudo kubectl get nodes
```
如果工作节点显示在列表中，且状态为 `Ready`，则表示工作节点成功加入集群。

```bash
sipeed@lpi3h-a2d1:~$ sudo kubectl get nodes
NAME         STATUS   ROLES                  AGE     VERSION
lpi3h-1967   Ready    <none>                 20h   v1.31.5+k3s1
lpi3h-231e   Ready    <none>                 20h   v1.31.5+k3s1
lpi3h-4782   Ready    <none>                 56m   v1.31.5+k3s1
lpi3h-a2d1   Ready    control-plane,master   23h   v1.31.5+k3s1
lpi3h-ba13   Ready    <none>                 19h   v1.31.5+k3s1
lpi3h-c06b   Ready    <none>                 21h   v1.31.5+k3s1
```

### 部署应用
我们新建一个配置文件，用于运行 k3s 容器

```bash
nano hello-kubernetes.yaml
```
文件内容如下：
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-kubernetes
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-kubernetes
  template:
    metadata:
      labels:
        app: hello-kubernetes
    spec:
      containers:
      - name: hello-kubernetes
        image: paulbouwer/hello-kubernetes:1.10.1
        env:
        - name: MESSAGE
          value: "Hello Kubernetes"
```
然后使用这个配置文件启动一个容器

```bash
sudo kubectl apply -f hello-kubernetes.yaml
```
查看 pods 状态

```bash
sudo kubectl get pods -o wide
NAME                                READY   STATUS    RESTARTS   AGE     IP            NODE   NOMINATED NODE   READINESS GATES
hello-kubernetes-7fbb7f4899-zqs5x   1/1     Running   0          2m39s   10.42.0.114   arch   <none>           <none>
```

通过浏览器访问 10.42.0.114:8080

![hello_k3s](./assets/hello_k3s.jpeg)