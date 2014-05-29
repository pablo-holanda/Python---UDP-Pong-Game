#ifndef PONG_H
#define PONG_H

#include <QWidget>

namespace Ui {
class Pong;
}

class Pong : public QWidget
{
    Q_OBJECT

public:
    explicit Pong(QWidget *parent = 0);
    ~Pong();

private:
    Ui::Pong *ui;
};

#endif // PONG_H
