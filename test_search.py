import os,sys
sys.path.append(os.getcwd())
import pytest
from search.base.base_driver import init_driver
from search.page.search_page import SearchPage
from search.base.base_yml import yal_data_with_file

# 抽取参数化输入内容作为函数
def data_key(key):
    return yal_data_with_file("search_data")[key]

class TestSearch:

    def setup(self):
        # 前置代码调用，连接手机
        self.driver = init_driver()
        # 调用连接手机操作对象，传递给self.search_page
        self.search_page = SearchPage(self.driver)

    # 参数化
    @pytest.mark.parametrize("content",data_key("test_search"))
    # 操作手机方式函数，调用类SearchPage各个方法
    def test_search(self,content):
        #点击放大镜
        self.search_page.click_search()
        # 输入文字
        self.search_page.input_text()
        # 点击返回
        self.search_page.click_back()
