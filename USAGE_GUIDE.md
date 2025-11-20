# 使用指南 / Usage Guide

## 项目文件说明 / Project Files

### 配置文件 / Configuration Files
- `capslox-karabiner.json` - 原始配置文件 (Original configuration)
- `capslox-karabiner-modified.json` - 改进的原始配置 (Modified original configuration)
- `capslox-karabiner-f19.json` - F19 版本配置 (F19 edition, generated)
- `capslox-karabiner-f20.json` - F20 版本配置 (F20 edition, generated)

### 脚本文件 / Script Files
- `generate_f19_config.py` - 生成 F19/F20 配置的脚本 (Configuration generator)
- `test_config.py` - 验证生成的配置文件 (Configuration validator)
- `compare_configs.py` - 比较不同配置的差异 (Configuration comparison tool)

### 文档文件 / Documentation Files
- `README.md` - 主文档 (Main documentation)
- `README_F19.md` - F19/F20 版本详细文档 (F19/F20 edition documentation)
- `USAGE_GUIDE.md` - 本文件 (This file)

---

## 快速开始 / Quick Start

### 1. 选择版本 / Choose Version

#### 使用原版 (适合大多数用户)
Use Original Version (for most users)

```bash
# 导入原版配置
karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/Alkacid/capslox-karabiner/main/capslox-karabiner-modified.json
```

#### 使用 F19/F20 版本 (如果遇到快捷键冲突)
Use F19/F20 Version (if you experience shortcut conflicts)

```bash
# 生成 F19 配置
python3 generate_f19_config.py

# 或生成 F20 配置
python3 generate_f19_config.py --key f20

# 复制到 Karabiner 配置目录
cp capslox-karabiner-f19.json ~/.config/karabiner/assets/complex_modifications/
```

### 2. 在 Karabiner-Elements 中启用 / Enable in Karabiner-Elements

1. 打开 Karabiner-Elements
2. 进入 "Complex Modifications" 标签页
3. 点击 "Add rule" 按钮
4. 选择相应的规则并启用

---

## 脚本使用详解 / Script Usage Details

### generate_f19_config.py - 配置生成器

#### 基本用法 / Basic Usage

```bash
# 使用默认设置生成 F19 配置
python3 generate_f19_config.py

# 生成 F20 配置
python3 generate_f19_config.py --key f20

# 指定输入和输出文件
python3 generate_f19_config.py input.json output.json

# 完整示例
python3 generate_f19_config.py capslox-karabiner-modified.json my-config.json --key f19
```

#### 命令行参数 / Command Line Arguments

```
python3 generate_f19_config.py [input_file] [output_file] [--key F19|F20]

参数说明:
  input_file    输入的 Karabiner 配置文件 (默认: capslox-karabiner-modified.json)
  output_file   输出的配置文件 (默认: capslox-karabiner-{key}.json)
  --key         使用的功能键 (f19 或 f20, 默认: f19)
  -h, --help    显示帮助信息
```

#### 输出示例 / Output Example

```
🔄 Transforming configuration...
   Input:  capslox-karabiner-modified.json
   Output: capslox-karabiner-f19.json
   Key:    F19

✅ Successfully generated capslox-karabiner-f19.json
   - Replaced Hyper modifier combo with F19 key
   - Updated version to 2.0.0
   - Transformed 64 manipulators
```

---

### test_config.py - 配置验证器

#### 用途 / Purpose
验证生成的配置文件是否正确转换，确保没有残留的 Hyper 修饰键组合。

Validates that generated configuration files are correctly transformed and contain no remaining Hyper modifier combinations.

#### 使用方法 / Usage

```bash
# 验证配置文件
python3 test_config.py
```

#### 输出示例 / Output Example

```
🧪 Testing generated configurations...

Testing capslox-karabiner-f19.json...
  ✅ All checks passed!

Testing capslox-karabiner-f20.json...
  ✅ All checks passed!

📊 Configuration Statistics:
   Total rules: 6
   Total manipulators: 64
   Version: 2.0.0

✅ All tests passed!
```

---

### compare_configs.py - 配置比较工具

#### 用途 / Purpose
比较原始配置和 F19/F20 配置，展示具体的差异和改进。

Compares original and F19/F20 configurations to show specific differences and improvements.

#### 使用方法 / Usage

```bash
# 比较所有配置
python3 compare_configs.py
```

#### 输出示例 / Output Example

```
📊 Comparing Configurations

🔵 Original Configuration (Hyper with modifier combo)
   Uses Hyper combo: 64 occurrences
   Capslock maps to: right_shift + modifiers

🟢 F19 Edition
   Uses F19: 63 occurrences
   Uses Hyper combo: 0 occurrences
   Capslock maps to: f19

💡 Key Differences:
   Original: Capslock → right_shift + right_command + right_control + right_option
   F19:      Capslock → f19 (single key, less conflicts)
```

---

## 完整工作流程 / Complete Workflow

### 从头开始设置 / Setup from Scratch

```bash
# 1. 克隆仓库
git clone https://github.com/Alkacid/capslox-karabiner.git
cd capslox-karabiner

# 2. 生成 F19 配置 (可选)
python3 generate_f19_config.py

# 3. 验证配置
python3 test_config.py

# 4. 比较配置差异
python3 compare_configs.py

# 5. 安装到 Karabiner-Elements
cp capslox-karabiner-f19.json ~/.config/karabiner/assets/complex_modifications/

# 6. 在 Karabiner-Elements 中启用规则
# (通过 GUI 操作)
```

### 更新现有配置 / Update Existing Configuration

```bash
# 1. 拉取最新更改
git pull

# 2. 重新生成配置
python3 generate_f19_config.py --key f19

# 3. 验证新配置
python3 test_config.py

# 4. 复制到配置目录
cp capslox-karabiner-f19.json ~/.config/karabiner/assets/complex_modifications/

# 5. 在 Karabiner-Elements 中重新加载配置
```

---

## 常见问题 / FAQ

### Q: 应该选择 F19 还是 F20？
**A:** 两者功能相同，都很少被使用。如果你不确定，选择 F19 即可。如果 F19 与其他软件冲突（极少见），可以尝试 F20。

### Q: 如何知道配置是否正确安装？
**A:** 
1. 运行 `python3 test_config.py` 验证配置文件
2. 在 Karabiner-Elements 的 "Complex Modifications" 中查看是否有对应规则
3. 测试 Capslock 键是否能触发映射的功能

### Q: F19/F20 版本与原版有什么区别？
**A:** 
- 原版: Capslock 映射到 right_shift + right_command + right_control + right_option
- F19/F20 版本: Capslock 映射到单个 F19 或 F20 键
- 优势: 更少冲突，更稳定，更容易调试

### Q: 我可以同时安装多个版本吗？
**A:** 可以，但同一时间只能启用一个版本的规则。在 Karabiner-Elements 中禁用一个版本的规则后再启用另一个版本。

### Q: 脚本需要什么依赖？
**A:** 脚本使用 Python 3 标准库，不需要额外安装任何依赖包。

### Q: 如何卸载？
**A:** 在 Karabiner-Elements 的 "Complex Modifications" 中移除相应规则，然后删除配置文件：
```bash
rm ~/.config/karabiner/assets/complex_modifications/capslox-karabiner-f19.json
```

---

## 故障排除 / Troubleshooting

### 问题: 脚本运行出错
```bash
# 检查 Python 版本 (需要 3.6+)
python3 --version

# 查看详细错误信息
python3 generate_f19_config.py 2>&1 | tee error.log
```

### 问题: 配置不生效
1. 确认 Karabiner-Elements 正在运行
2. 检查规则是否已启用
3. 重启 Karabiner-Elements
4. 查看 Karabiner-Elements 日志

### 问题: 按键冲突
1. 尝试切换到 F20 版本
2. 检查其他软件的快捷键设置
3. 在 Karabiner-Elements 中调整规则优先级

---

## 贡献 / Contributing

欢迎提交问题和改进建议！

Welcome to submit issues and improvement suggestions!

- 报告 Bug: [GitHub Issues](https://github.com/Alkacid/capslox-karabiner/issues)
- 提交改进: [Pull Requests](https://github.com/Alkacid/capslox-karabiner/pulls)

---

## 参考链接 / References

- [Karabiner-Elements 官网](https://karabiner-elements.pqrs.org/)
- [Karabiner 配置文档](https://karabiner-elements.pqrs.org/docs/)
- [原项目](https://github.com/Alkacid/capslox-karabiner)
