# Created by Vanessa at 03/02/2019
Feature: Settings

  Background:
    Given the app "whatsapp" is open
    And the "settings" screen is open

  Scenario: Settings - Change profile name
    And the "profile" option is chosen
    Then it will be possible to change the name

  Scenario: Settings - Favorite Messages
    And the "favorite messages" option is chosen
    Then it will be possible to see all the save messages
