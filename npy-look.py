import numpy as np
import os


def view_npy_file(file_path):
    """
    简单查看.npy文件内容
    """
    print(f"📁 正在查看文件: {file_path}")

    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"❌ 文件不存在: {file_path}")
        return

    try:
        # 加载.npy文件
        data = np.load(file_path)

        print(f"📊 数据类型: {type(data)}")
        print(f"🔢 数组形状: {data.shape}")
        print(f"💾 数据类型: {data.dtype}")
        print(f"📏 数组维度: {data.ndim}D")
        print(f"📊 元素总数: {data.size:,}")
        print("-" * 50)

        # 显示统计信息
        print("📈 统计信息:")
        print(f"  最小值: {data.min():.6f}")
        print(f"  最大值: {data.max():.6f}")
        print(f"  平均值: {data.mean():.6f}")
        print(f"  标准差: {data.std():.6f}")
        print(f"  中位数: {np.median(data):.6f}")

        print("-" * 50)

        # 显示部分数据
        print("📝 数据预览:")
        if data.ndim == 1:
            # 一维数组
            if data.size <= 20:
                print(f"  全部数据: {data}")
            else:
                print(f"  前10个: {data[:10]}")
                print(f"  后10个: {data[-10:]}")

        elif data.ndim == 2:
            # 二维数组
            if data.shape[0] <= 10 and data.shape[1] <= 10:
                print("  完整矩阵:")
                print(data)
            else:
                print("  左上角 5x5 子矩阵:")
                print(data[:5, :5])

        else:
            # 高维数组
            print(f"  第一个元素的形状: {data[0].shape}")
            if data[0].size <= 20:
                print(f"  第一个元素: {data[0]}")
            else:
                print(f"  第一个元素的前10个值: {data[0].flatten()[:10]}")

    except Exception as e:
        print(f"❌ 加载失败: {e}")


# 使用示例
if __name__ == "__main__":
    # 替换为你的.npy文件路径
    file_path = "F:/github/bishe/tosc-jieguo/jsc_parameters - 2/CIFAR10_AWGN_params.npy"  # 修改这里!

    view_npy_file(file_path)