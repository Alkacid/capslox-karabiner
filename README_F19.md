# Capslox Karabiner - F19 Edition

## 概述 (Overview)

这是 capslox-karabiner 的改进版本，将 Hyper 键从同时按下多个修饰键（right_command + right_control + right_option + right_shift）改为使用 F19 键。这样可以避免在某些应用程序中产生意外的按键冲突。

This is an improved version of capslox-karabiner that replaces the Hyper key implementation from simultaneously pressing multiple modifier keys (right_command + right_control + right_option + right_shift) to using the F19 key. This avoids unexpected key conflicts in some applications.

## 主要变化 (Key Changes)

### 原版本 (Original Version)
- Capslock → right_shift + right_command + right_control + right_option
- 可能与某些应用的快捷键冲突

### F19 版本 (F19 Edition)
- Capslock → F19
- F19 是一个很少使用的功能键，不会与其他快捷键冲突
- 所有 Capslock + 其他键的组合现在使用 F19 作为修饰键

## 生成配置文件 (Generate Configuration)

使用提供的 Python 脚本生成 F19 版本的配置文件：

```bash
python3 generate_f19_config.py [input_file] [output_file]
```

默认参数：
- input_file: `capslox-karabiner-modified.json`
- output_file: `capslox-karabiner-f19.json`

示例 (Examples)：
```bash
# 使用默认文件名
python3 generate_f19_config.py

# 指定输入输出文件
python3 generate_f19_config.py my-config.json my-config-f19.json
```

## 安装 (Installation)

### 方法 1: 本地文件导入 (Local File Import)

1. 生成配置文件：
   ```bash
   python3 generate_f19_config.py
   ```

2. 将生成的 `capslox-karabiner-f19.json` 复制到 Karabiner-Elements 配置目录：
   ```bash
   cp capslox-karabiner-f19.json ~/.config/karabiner/assets/complex_modifications/
   ```

3. 打开 Karabiner-Elements，进入 "Complex Modifications" 标签页

4. 点击 "Add rule" 按钮，选择 "capslox-karabiner (F19 Edition)"

5. 启用所需的规则

### 方法 2: URL 导入 (URL Import)

如果配置文件托管在 GitHub 上，可以使用以下 URL 格式导入：

```
karabiner://karabiner/assets/complex_modifications/import?url=https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/capslox-karabiner-f19.json
```

## 功能说明 (Features)

所有功能与原版本相同，只是触发方式从"多个修饰键组合"改为"F19"：

### Capslock 映射
| 按键 | 映射为 | 说明 |
|------|--------|------|
| `⇪` 单击 | `caps_lock` | 单击切换大写锁定 |
| `⇪` 长按 | `F19` | 按住 Capslock 作为 F19 修饰键 |
| `⇪` + `spacebar` | `ctrl` + `spacebar` | 切换输入法 |

### 光标移动 (Cursor Movement)
| 按键 | 映射为 | 说明 |
|------|--------|------|
| `⇪` + `E` | `↑` | 向上移动 |
| `⇪` + `D` | `↓` | 向下移动 |
| `⇪` + `S` | `←` | 向左移动 |
| `⇪` + `F` | `→` | 向右移动 |
| `⇪` + `A` | `option` + `←` | 向左移动一个单词 |
| `⇪` + `G` | `option` + `→` | 向右移动一个单词 |

... (其他功能保持不变，详见主 README.md)

## 优势 (Advantages)

1. **减少冲突**: F19 很少被应用程序使用，避免了与其他快捷键的冲突
2. **更稳定**: 不会触发系统或应用程序中预设的多修饰键组合
3. **兼容性更好**: 在各种应用程序中表现更加一致
4. **易于调试**: 如果出现问题，更容易识别是 F19 键的问题

## 技术细节 (Technical Details)

脚本会进行以下转换：

1. 将 Capslock 的 `to` 映射从 `right_shift + modifiers` 改为 `f19`
2. 将所有 `mandatory` 修饰键数组中的 Hyper 组合替换为 `f19`
3. 保留其他修饰键（如 `left_command`）与 F19 的组合
4. 保持所有其他配置不变（如 `to_if_alone`、条件等）

## 故障排除 (Troubleshooting)

### F19 不工作
- 确保 Karabiner-Elements 正在运行
- 检查规则是否已启用
- 重启 Karabiner-Elements

### 某些按键不响应
- 查看 Karabiner-Elements 的日志
- 确认应用程序没有被排除在外（bundle_identifiers）

## 参考 (References)

- [Karabiner-Elements](https://karabiner-elements.pqrs.org/)
- [原项目 (Original Project)](https://github.com/Alkacid/capslox-karabiner)
