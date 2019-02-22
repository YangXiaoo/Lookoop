/**
 * 2019-2-14
 *
**/

import java.util.List
import java.util.ArrayList;


public class Person {
	private String name;
	private String gender;
	private String marialStatus;

	public Person(String name, String gender, String marialStatus) {
		this.name = name;
		this.gender = gender;
		this.marialStatus = marialStatus;
	}

	public String getName() {
		return this.name;
	}

	public String getGender() {
		return this.gender;
	}
	public String getMaritalStatus() {
		return this.maritalStatus;
	}
}


public interface Criteria {
	public List<Person> meetCriteria(List<Person> person) {

	}
}


public class CriteriaMale implements Criteria {
	@Override
	public List<Person> meetCriteria(List<Person> persons) {
		List<Person> malePersons = new ArrayList<Person>();
		for (Person person : persons) {
			if (person.getGender().equalsIgnoreCase("MALE")) {
			malePersons.add(person);
			}
		}
		return malePersons;
	}
}

public class CriteriaFemale implements Criteria {
	@Override
	public List<Person> meetCriteria(List<Person> persons) {
		List<Person> femalePersons = new ArrayList<Person>();
		for (Person person : persons) {
			if (person.getGender().equalsIgnoreCase("FEMALE")){
				femalePersons.add(person);
			}
		}
		return femalePersons;
	}



public class CriteriaSingle implements Criteria {
	@Override
	public List<Person> meetCriteria(List<Person> persons) {
		List<Person> singlePersons = new ArrayList<Person>();
		for (Person person : persons) {
			if (person.getMaritalStatus().equalsIgnoreCase("SINGLE")){
				singlePersons.add(person);
			}
		}
	return singlePersons;
	}
}

import java.util.List;
public class AndCriteria implements Criteria {
	private Criteria criteria;
	private Criteria otherCriteria;
	public AndCriteria(Criteria criteria, Criteria otherCriteria) {
		this.criteria = criteria;
		this.otherCriteria = otherCriteria;
	}
	@Override
	public List<Person> meetCriteria(List<Person> persons) {
		List<Person> firstCriteriaPersons = criteria.meetCriteria(persons);
		return otherCriteria.meetCriteria(firstCriteriaPersons);
	}
}



public class OrCriteria implements Criteria {
	private Criteria criteria;
	private Criteria otherCriteria;
	public OrCriteria(Criteria criteria, Criteria otherCriteria) {
		this.criteria = criteria;
		this.otherCriteria = otherCriteria;
	}
	@Override
	public List<Person> meetCriteria(List<Person> persons) {
		List<Person> firstCriteriaItems = criteria.meetCriteria(persons);
		List<Person> otherCriteriaItems = otherCriteria.meetCriteria(persons);
		for (Person person : otherCriteriaItems) {
			if (!firstCriteriaItems.contains(person)){
				firstCriteriaItems.add(person);
			}
		}
		return firstCriteriaItems;
	}
}


public class CriteriaPatternDemo {
	public static void main(String[] args) {
		List<Person> persons = new ArrayList<Person>();
		persons.add(new Person("Robert","Male", "Single"));
		persons.add(new Person("John","Male", "Married"));
		persons.add(new Person("Laura","Female", "Married"));
		persons.add(new Person("Diana","Female", "Single"));
		persons.add(new Person("Mike","Male", "Single"));
		persons.add(new Person("Bobby","Male", "Single"));
		Criteria male = new CriteriaMale();
		Criteria female = new CriteriaFemale();
		Criteria single = new CriteriaSingle();
		Criteria singleMale = new AndCriteria(single, male);
		Criteria singleOrFemale = new OrCriteria(single, female);
		System.out.println("Males: ");
		printPersons(male.meetCriteria(persons));
		System.out.println("\nFemales: ");
		printPersons(female.meetCriteria(persons));
		System.out.println("\nSingle Males: ");
		printPersons(singleMale.meetCriteria(persons));
		System.out.println("\nSingle Or Females: ");
		printPersons(singleOrFemale.meetCriteria(persons));
	}
	public static void printPersons(List<Person> persons){
		for (Person person : persons) {
			System.out.println("Person : [ Name : " + person.getName()
			+", Gender : " + person.getGender()
			+", Marital Status : " + person.getMaritalStatus()
			+" ]");
		}
	}
}


/*
	Males: 
	Person : [ Name : Robert, Gender : Male, Marital Status : Single ]
	Person : [ Name : John, Gender : Male, Marital Status : Married ]
	Person : [ Name : Mike, Gender : Male, Marital Status : Single ]
	Person : [ Name : Bobby, Gender : Male, Marital Status : Single ]

	Females: 
	Person : [ Name : Laura, Gender : Female, Marital Status : Married ]
	Person : [ Name : Diana, Gender : Female, Marital Status : Single ]

	Single Males: 
	Person : [ Name : Robert, Gender : Male, Marital Status : Single ]
	Person : [ Name : Mike, Gender : Male, Marital Status : Single ]
	Person : [ Name : Bobby, Gender : Male, Marital Status : Single ]

	Single Or Females: 
	Person : [ Name : Robert, Gender : Male, Marital Status : Single ]
	Person : [ Name : Diana, Gender : Female, Marital Status : Single ]
	Person : [ Name : Mike, Gender : Male, Marital Status : Single ]
	Person : [ Name : Bobby, Gender : Male, Marital Status : Single ]
	Person : [ Name : Laura, Gender : Female, Marital Status : Married ]
*/