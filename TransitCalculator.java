/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package transitfare;

/**
 *
 * @author kmich
 */
import java.lang.Math;

public class TransitCalculator {
    int days;
    int rides;
    Double[] fares = {2.75,33.00,127.00};
    
    public TransitCalculator(int numDays, int numRides) {
      days = numDays;
      rides = numRides;
    }
    
    public static double unlimited7Price (int days, int rides, Double[] fares) {
        double fare = fares[1];
        if (days > 30) {
            System.out.println("Number of days is too long.  Try again with less than 30 days.");
        } else {
            double num = Math.ceil(days/7) + 1;
            fare = fares[1]*num/rides;
        }
        return fare;
    }
    
    public static Double[] getRidePrices (int days, int rides, Double [] fares) {
      Double[] allFares = fares;
      
      //leave single fare alone - so allFares[0] = fare[0]
      
      allFares[1] = unlimited7Price(days,rides,fares);
      
      //For 30-day unlimited, price per ride is simply total/# of rides
      allFares[2] = fares[2]/rides;
      
      return allFares;
    }
    
    public static String getBestFare (Double[] allFares) {
        String statement = "";
        double min = allFares[0];
        String type = "Pay-per-ride";
        
        for (int i = 1; i < allFares.length; i++) {
            if (allFares[i] < min) {
                min = allFares[i];
                if (i == 1) {
                    type = "7-day Unlimited";
                } else {
                    type = "30-day Unlimited";
                }
            }
        }
        
        statement = "You should get the " + type + " at " + min + " per ride.";
        
        return statement;
    }

    public static void main(String[] args) {
        // TODO code application logic here
        TransitCalculator NYC = new TransitCalculator(14,50);
        //System.out.println(unlimited7Price(NYC.days, NYC.rides, NYC.fares)); 
        Double[] ridePrices = getRidePrices(NYC.days,NYC.rides, NYC.fares);      
        String lowestFare = getBestFare(ridePrices);
        System.out.println(lowestFare);
       
    }
    
}
