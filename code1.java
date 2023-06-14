import java.time.*;
import java.time.DayOfWeek;

class DayOfWeekExample {

public static void main(String[] args) 
{ 
LocalDate localDate = LocalDate.of(1947,Month.AUGUST, 15); 
DayOfWeek dayOfWeek = DayOfWeek.from(localDate); 
System.out.println("Day of the Week on"+ " 15th August 1947 - " + dayOfWeek.name()); 
int val = dayOfWeek.getValue(); 
System.out.println("Int Value of " + dayOfWeek.name() + " - " + val); 
} 

}