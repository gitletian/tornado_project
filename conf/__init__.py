# coding: utf-8
# __author__: ""

import os
from .config import dev

# 加载 配置文件
dev.update(
    template_path=os.path.join(os.path.dirname(__file__), "../templates"),
    static_path=os.path.join(os.path.dirname(__file__), "../static"),
)


settings = dev

