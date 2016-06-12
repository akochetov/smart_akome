//CommunicationMethod enum
CommunicationMethodSend = 1;
CommunicationMethodReceive = 2;
CommunicationMethodBoth = 3;

(function (ko, datacontext) {
    datacontext.Device = Device;
    datacontext.Signal = Signal;

    //datacontext.triggerMessage = ko.observable();

    function Device(data) {
        var self = this;
        data = data || {};       
        
        // Persisted properties
        self.ID = data.ID;
        self.Name = data.Name;
        self.CommunicationMethod = data.CommunicationMethod;
        self.signals = ko.observableArray(importSignals(data.Signals));
        self.errorMessage = ko.observable();

        self.toJson = function () { return ko.toJSON(self) };        
    };

    function importSignals(signals) {        
        return $.map(signals || [],
                function (signalData) {                    
                    return datacontext.createSignal(signalData);
                });
    }

    function Signal(data) {
        var self = this;
        data = data || {};

        // Persisted properties
        self.ID = data.ID;
        self.DeviceID = data.DeviceID;
        self.Name = data.Name;
        self.SignalDirection = data.SignalDirection;        
        self.Pattern = data.Pattern
        self.errorMessage = ko.observable();        
        
        self.triggerSignal = function () {
            var signal = this;
            return datacontext.triggerSignal(signal)
                 .done(function () { });
        };

        self.toJson = function () { return ko.toJSON(self) };        
    };
})(ko, App.datacontext);