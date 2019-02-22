#include <iostream>
using namespace std;
#define  free_ptr(p) \
	if(p) delete p; p = NULL;
 
class IWind{
public:
	virtual ~IWind(){};
	virtual void blowWind() = 0;
};
 
class ColdWind : public IWind{
public:
	void blowWind(){
		cout<<"Blowing cold wind!"<<endl;
	};
};
 
class WarmWind : public IWind{
public:
	void blowWind(){
		cout<<"Blowing warm wind!"<<endl;
	}
};
 
class NoWind : public IWind{
public:
	void blowWind(){
		cout<<"No Wind!"<<endl;
	}
};


class WindMode{
public:
	WindMode(IWind* wind): m_wind(wind){};
	~WindMode(){free_ptr(m_wind);}
	void blowWind(){
		m_wind->blowWind();
	};
private:
	IWind* m_wind;
};


int main(int argc, char* argv[])
{
	WindMode* warmWind = new WindMode(new WarmWind());
	WindMode* coldWind = new WindMode(new ColdWind());
	WindMode* noWind = new WindMode(new NoWind());
 
	warmWind->BlowWind();
	coldWind->BlowWind();
	noWind->BlowWind();
 
	free_ptr(warmWind);
	free_ptr(coldWind);
	free_ptr(noWind);
	system("pause");
	return 0;
}
