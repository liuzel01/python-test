# from templater import DefaultTemplater
#
# templater = DefaultTemplater("untemplated.txt", "templated.txt")
# tag = {"test": "Hello world"}
# templater.render(tag)



from templater import DefaultTemplater

if __name__ == "__main__":

    templater = DefaultTemplater("report.html", "report_templeted.html")
    rows = [
        {
            "turnover": 1607.2,
            "quantity": 49,
            "country": "Germany",
        },
        {
            "turnover": 281.6,
            "quantity": 16,
            "country": "Portugal",
        },
        {
            "turnover": 7.3,
            "quantity": 1,
            "country": "Spain",
        },
        {
            "turnover": 35.0,
            "quantity": 5,
            "country": "France",
        },
    ]
    columns = list(rows[0].keys())
    metrics = ["quantity", "turnover"]
    dimension = ["country"]
    tags = {
        "date": "'August 2020'",
        "metrics": metrics,
        "dimension": dimension,
        "rows": rows,
        "columns": columns
    }
    templater.render(tags)
