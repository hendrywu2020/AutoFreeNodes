import logging

def write_subscribe_link(subscribe_link, filename):
    try:
        with open(filename, 'w') as f:
            f.write(subscribe_link)
        logging.info(f"订阅链接已写入到文件: {filename}")
    except Exception as e:
        logging.error(f"写入订阅链接到文件 {filename} 失败: {e}")

if __name__ == '__main__':
    # 示例用法
    test_link = "base64_encoded_v2ray_subscribe_link"
    write_subscribe_link(test_link, 'v2ray_subscribe.txt')
