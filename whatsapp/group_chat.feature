# Created by Vanessa at 03/02/2019
Feature: Group chat

  Background:
    Given the app "whatsapp" is open

  Scenario: Group chat - Check received message
    When sent the message "Hello" to "Group A"
    And open the message data
    Then check if "Person 1" received the message

  Scenario: Group chat - Send conversation to email
    When choose a conversation
    And the "export conversation" option is chosen
    Then check if the content of the conversation has been received