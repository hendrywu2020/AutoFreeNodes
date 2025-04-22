# AutoFreeNodes

一个自动抓取 V2Ray 和 Hysteria2 免费节点并生成 V2Ray 订阅链接的开源项目。

**警告：**

* **免费节点通常不稳定且质量不高，请自行承担使用风险。**
* **抓取某些网站的数据可能涉及法律和道德问题，请务必遵守相关网站的服务条款和法律法规。**
* **本项目仅供学习交流使用，请勿用于非法用途。**

## 功能特性

* 定期自动抓取 V2Ray 免费节点。
* 尝试抓取 Hysteria2 免费节点。
* 将抓取到的 V2Ray 节点信息转换为标准的 V2Ray 订阅链接格式。
* 将生成的订阅链接输出到 `output/v2ray_subscribe.txt` 文件。
* 可通过配置文件自定义节点来源网址和抓取间隔。
* 记录程序运行日志。

## 如何使用

1.  **克隆仓库：**
    ```bash
    git clone <你的 GitHub 仓库地址>
    cd AutoFreeNodes
    ```

2.  **安装依赖：**
    ```bash
    pip install requests beautifulsoup4 schedule
    ```

3.  **配置：**
    编辑 `config/config.ini` 文件，修改 `v2ray_urls` 和 `hysteria2_urls` 配置项，添加你想要抓取的免费节点分享网址。你可以添加多个网址，用逗号分隔。同时，可以修改 `interval_minutes` 设置抓取间隔（单位：分钟）。

4.  **运行：**
    ```bash
    python main.py
    ```
    程序将在后台运行，并按照设定的时间间隔抓取节点信息，并将订阅链接更新到 `output/v2ray_subscribe.txt` 文件中。你可以在 `logs/auto_free_nodes.log` 文件中查看运行日志。

5.  **使用订阅链接：**
    将 `output/v2ray_subscribe.txt` 文件中的内容复制到你的 V2Ray 客户端的订阅设置中。

## 注意事项

* 由于免费节点来源不稳定，抓取成功率和节点质量无法保证。
* 请定期检查 `config/config.ini` 中的网址是否仍然有效。
* 本项目目前可能无法完美地将所有 Hysteria2 节点转换为 V2Ray 可用的格式，具体实现取决于技术可行性。

## 未来计划

* 优化节点抓取和解析逻辑，提高成功率和鲁棒性。
* 尝试支持更多类型的节点和订阅格式。
* 考虑通过 Web API 的方式提供订阅链接。
* 增加节点过滤和去重功能。

## 贡献

欢迎贡献你的代码和想法！你可以通过以下方式参与项目：

* 提交 Issue 报告 Bug 或提出建议。
* 提交 Pull Request 贡献代码。

## 许可证

[请在此处添加你的开源许可证，例如 MIT License](LICENSE)

## 免责声明

本项目仅供学习交流使用，不对因使用本项目产生的任何问题负责。请遵守当地法律法规。