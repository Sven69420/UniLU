package garden.plants;

import garden.Ornament;

/**
 * This abstract class provides a foundation for all other plant types in the garden 
 * by defining the common characteristics all plants share, such as Name and Water Consumption
 */

public abstract class Plant implements Ornament {
	protected String name; 
	protected double waterConsumption; // Daily Water consumption
	
	// Constructor for the Plant Class
	public Plant(String name, double waterConsumption) {
		this.name = name;
		this.waterConsumption = waterConsumption;
	}
	
	// Calculates the total water used by the plant over a given period of Days
	public double consumedWater(int days) {
		return days * waterConsumption;
	}
	
	// Gets the Name of the Plant
	@Override
	public String getName() {
		return name;
	}
}
