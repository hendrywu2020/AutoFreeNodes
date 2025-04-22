import schedule
import time
import logging
import configparser
from crawler.v2ray_crawler import fetch_v2ray_nodes
from crawler.hysteria2_crawler import fetch_hysteria2_nodes
from converter.v2ray_converter import convert_to_v2ray_subscribe
from output.output_handler import write_subscribe_link

# 配置日志
logging.basicConfig(filename='logs/auto_free_nodes.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 加载配置
config = configparser.ConfigParser()
config.read('config/config.ini')

def job():
    logging.info("开始执行节点抓取任务...")
    v2ray_urls = [url.strip() for url in config['sources']['v2ray_urls'].split(',')]
    hysteria2_urls = [url.strip() for url in config['sources']['hysteria2_urls'].split(',')]

    v2ray_nodes = fetch_v2ray_nodes(v2ray_urls)
    hysteria2_nodes = fetch_hysteria2_nodes(hysteria2_urls)

    all_nodes = v2ray_nodes + hysteria2_nodes # 可以根据需要修改合并逻辑

    if all_nodes:
        subscribe_link = convert_to_v2ray_subscribe(all_nodes)
        write_subscribe_link(subscribe_link, 'output/v2ray_subscribe.txt')
        logging.info(f"成功抓取并生成订阅链接，共 {len(all_nodes)} 个节点。")
    else:
        logging.warning("未抓取到任何节点。")

if __name__ == "__main__":
    schedule.every(int(config['schedule']['interval_minutes'])).minutes.do(job)
    logging.info(f"定时任务已启动，每 {config['schedule']['interval_minutes']} 分钟执行一次。")
    while True:
        schedule.run_pending()
        time.sleep(1)
