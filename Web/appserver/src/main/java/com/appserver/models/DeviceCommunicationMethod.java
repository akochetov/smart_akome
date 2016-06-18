package com.appserver.models;

/**
 * Enum, contains device communication ways, e.g. send, receive etc.
 */
public enum DeviceCommunicationMethod {
   	/**
   	 * Device can only send signals
   	 */
    Send(1),
    /**
     * Device can only receive signals
     */
    Receive(2),
    /**
     * Device can send and receive signals
     */
    Both(3);
    
    private final int value;
    private DeviceCommunicationMethod(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}
