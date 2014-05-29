#include "pong.h"
#include "ui_pong.h"

Pong::Pong(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Pong)
{
    ui->setupUi(this);
}

Pong::~Pong()
{
    delete ui;
}
