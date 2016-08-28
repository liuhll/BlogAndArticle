# KVM教程
> - [Kvm教程](http://wiki.ubuntu.org.cn/Kvm%E6%95%99%E7%A8%8B)
> - [Kvm简单教程](http://wiki.ubuntu.org.cn/Kvm%E7%AE%80%E5%8D%95%E6%95%99%E7%A8%8B)

## 介绍
- KVM（Kernel-based Virtual Machine）
> 基于内核的虚拟机，配合QEMU（处理器虚拟软件），需要CPU支持虚拟化技术（并且在BIOS里打开虚拟化选项），效率可达到物理机的80％以上。此外，它对SMP的支持很好
- 关于kvm
  - kvm是开源软件，全称是`kernel-based virtual machine`（基于内核的虚拟机）。
  - 是x86架构且硬件支持虚拟化技术（如 intel VT 或 AMD-V）的linux [全虚拟化] 解决方案
  - 包含一个为处理器提供底层虚拟化 可加载的核心模块kvm.ko（kvm-intel.ko 或 kvm-AMD.ko)
  - kvm还需要一个经过修改的QEMU软件（qemu-kvm），作为虚拟机上层控制和界面。
  - kvm能在不改变linux或windows镜像的情况下**同时运行多个虚拟机**（ps：它的意思是多个虚拟机使用同一镜像），并为每一个虚拟机配置个性化硬件环境
  - 主流的linux内核，如2.6.20以上的内核均包含了kvm核心

## 与其他虚拟化产品对比
1. `Vmware`的功能全面，设置全面，速度相对最慢；
2. `VirtualBox`的效率比`Vmware`高一些，中文用户最多；
3. `KVM`**整体效率最高**。

## 如何查明你的系统是否能运行KVM?
1. 通过上网查询当前的处理器是否在其中
2. 检查`/proc/cpuinfo`，如果在`cpu flags`字段看到了`vmx(Intel)`或`svm(AMD)`，那么你的处理器就支持KVM
```
egrep '(vmx|svm)' /proc/cpuinfo
```

## 管理工具（CLI——命令行 或 Desktop——桌面 或 WEB——网络）

## qemu 
- 全称`Quick Emulator`： 独立虚拟软件，能独立运行虚拟机
- `kqemu`是该软件的加速软件
- **kvm并不需要qemu进行虚拟处理**，只是需要它的上层管理界面进行虚拟机控制
## 创建虚拟镜像
```
kvm-img create xxx.img 2G
```

### 安装虚拟机系统
```
kvm -drive file=xxxx.img -cdrom /path/to/boot-media.iso -boot d -m 512
```
