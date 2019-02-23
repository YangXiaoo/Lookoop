//工厂方法模式
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
class Factory//工厂类
{
	public:
	virtual Product *createProduct()=0;
};

class FactoryA:public Factory{
	public:
	Product *createProduct(){
		return new ProductA();
		}
};

class FactoryB:public Factory{
	public:
	Product *createProduct(){
		return new ProductB();
		}
};
class FactoryC:public Factory{
	public:
	Product *createProduct(){
		return new ProductC();
		}
};
int main()
{
	Factory *factoryA=new FactoryA();
	Product *productA = factoryA->createProduct();
	productA->Show();
	Factory *factoryB=new FactoryB();
	Product *productB = factoryB->createProduct();
	productB->Show();
	if (factoryA)
	{
	delete factoryA;
	factoryA = NULL;
	}
	if (factoryB)
	{
	delete factoryB;
	factoryB = NULL;
	}
	if (productA)
	{
	delete productA;
	productA = NULL;
	}
	if (productB)
	{
	delete productB;
	productB = NULL;
	}
	return 0;
}
