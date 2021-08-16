
from templater import DefaultTemplater

if __name__ == "__main__":

    templater = DefaultTemplater("bar-simple.html", "bar-simple-templeted.html")
    data1 = ['张三1', '李四2', '王五3', '赵六4']
    data2 = [3120, 3200, 3150, 980]
    tags = {
        "data1": data1,
        "data2": data2,
    }
    templater.render(tags)