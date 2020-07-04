on run {targetBuddyPhone, targetMessage}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetBuddyPhone of targetService
        repeat 100 times
        send targetMessage to targetBuddy 
        end repeat 
    end tell
    
end run

