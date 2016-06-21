package com.appserver.models;

import com.google.gson.annotations.SerializedName;

/**
 * Defines signal type, if it is a signal coming from or to device
 */
public enum SignalDirection {
   	/**
   	 * Signal coming to device
   	 */
	@SerializedName("1")
	ToDevice(1),
    /**
     * Signal coming from device
     */
	@SerializedName("2")
    FromDevice(2);
    
    private final int value;
    private SignalDirection(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}
