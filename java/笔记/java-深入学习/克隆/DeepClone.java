// 2019-6-19
// https://blog.csdn.net/qq_38962004/article/details/79721230

class Profile implements Cloneable {
	private String 	email;

	Profile(String email) {
		this.email = email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getEmail() {
		return email;
	}

	@Override
	public Object clone() {
		Profile profile = null;
    	try {
    		profile = (Profile)super.clone();	// 浅复制
    	} catch (CloneNotSupportedException e) {
    		e.printStackTrace();
    	}

    	return profile;
	}
}


class Person implements Cloneable {
    private int age;
    private String name;
    private Profile profile;

    Person(String name, int age, Profile profile) {
    	this.name = name;
    	this.age = age;
    	this.profile = profile;
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setProfile(Profile profile) {
    	this.profile = profile;
    }

    public Profile getProfile() {
    	return profile;
    }

    @Override
    public Person clone() {
    	Person person = null;
    	try {
    		person = (Person)super.clone();	// 浅复制
    	} catch (CloneNotSupportedException e) {
    		e.printStackTrace();
    	}

    	person.setProfile((Profile)profile.clone());	// 深复制

    	return person;
    }
}


class DeepClone {
	public static void test1() {
		Profile profile = new Profile("1270009836@qq.com");
		Person person = new Person("a", 10, profile);
        System.out.println("person, email is :" + person.getProfile().getEmail());

		Person personClone = person.clone();
		personClone.getProfile().setEmail("1593606228@qq.com");
		System.out.println("After clone:");
        System.out.println("person, email is :" + person.getProfile().getEmail());
		System.out.println("personClone, email is :" + personClone.getProfile().getEmail());

	}
	public static void main(String[] args) {
		test1();
	}
}
// person, email is :1270009836@qq.com
// After clone:
// person, email is :1270009836@qq.com
// personClone, email is :1593606228@qq.com