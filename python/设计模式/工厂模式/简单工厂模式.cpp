//简单工厂模式
typedef enum ProductTypeTag
{
	TypeA,
	TypeB,
	TypeC
}PRODUCTTYPE;


class Product//产品抽象基类
{
public:
	virtual void Show() = 0;
};


class ProductA : public Product
{
public:
	void Show()
	{
	cout<<"I'm ProductA"<<endl;
	}
};

class ProductB : public Product
{
public:
	void Show()
	{
	cout<<"I'm ProductB"<<endl;
	}
};


class ProductC : public Product
{
public:
	void Show()
	{
	cout<<"I'm ProductC"<<endl;
	}
};

class Factory//工厂类
{
public:
	Product* CreateProduct(PRODUCTTYPE type)
	{
	switch (type)
	{
		case TypeA:
		return new ProductA();
		case TypeB:
		return new ProductB();
		case TypeC:
		return new ProductC();
		default:
		return NULL;
		}
	}
};

int main()
{
	Factory productCreator;
	Product *productA=productCreator.CreateProduct(TypeA);
	Product *productB=productCreator.CreateProduct(TypeB);
	Product *productC=productCreator.CreateProduct(TypeC);
	productA->Show();
	productB->Show();
	productC->Show();
	if(productA){
	delete productA;
	productA=NULL;
	}
	if(productB){
	delete productB;
	productB=NULL;
	}
	if(productC){
	delete productC;
	productC=NULL;
	}
	return 0;
}
