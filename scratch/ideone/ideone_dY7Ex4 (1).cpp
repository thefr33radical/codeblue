#include <QJsonObject>
#include <QJsonArray>
#include <QJsonDocument>
#include <QDebug>

int main(int argc, char *argv[])
{
    QJsonObject topQuery;
    topQuery["objectType"] = QString("objects.Word");

    QJsonObject parameters;
    parameters["language"] = QString("en");
    parameters["to"] = QString("ru");
    parameters["rate"] = 0;
    parameters["isInput"] = true;

    topQuery["query"] = parameters;

    QJsonObject sortParameter;
    sortParameter["sortBy"] = QString("rate");
    sortParameter["direction"] = QString("desc");

    QJsonArray sortArray;
    sortArray.append(sortParameter);

    topQuery["sort"] = sortArray;
    topQuery["limit"] = 10;

    QJsonDocument document(topQuery);
    qDebug() << document.toJson();
}
