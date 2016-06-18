package com.appserver.models;

/**
 * Defines signal type, if it is a signal coming from or to device
 */
public enum SignalDirection {
   	/**
   	 * Signal coming to device
   	 */
	ToDevice(1),
    /**
     * Signal coming from device
     */
    FromDevice(2);
    
    private final int value;
    private SignalDirection(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}
