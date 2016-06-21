package com.appserver.models;

import com.google.gson.annotations.SerializedName;

/**
 * Enum, contains device communication ways, e.g. send, receive etc.
 */
public enum DeviceCommunicationMethod {
   	/**
   	 * Device can only send signals
   	 */
	@SerializedName("1")
    Send(1),
    /**
     * Device can only receive signals
     */
    @SerializedName("2")
    Receive(2),
    /**
     * Device can send and receive signals
     */
    @SerializedName("3")
    Both(3);
    
    private final int value;
    private DeviceCommunicationMethod(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}
