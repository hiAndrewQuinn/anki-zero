# Anki Zero: Never miss your reviews again - or else 💸

Anki's value add is all in the reviews, yet all too often we let ourselves procrastinate
on the most important part of the whole program. Not anymore! **Anki Zero** is a
simple plugin to integrate Anki with Beeminder, with one goal in mind: **If you
don't complete your "Due" and "Learning" columns, you get charged a fine.**

## Getting Started

Follow these simple steps to start using the Anki to Beeminder Sync Plugin:

1. **Create a Beeminder "Whittle Down" Goal called `anki-zero`:** Before you begin, create a "Whittle Down" goal in your Beeminder account. Name the goal `anki-zero` to represent your Anki progress tracking.

2. **Install the Plugin:** Install the Anki to Beeminder Sync Plugin by adding it to your Anki addons. You can do this by going to the "Tools" menu in Anki, selecting "Add-ons," and then choosing "Get Add-ons." Enter the addon code [ADDON_CODE_HERE] to install the plugin.

3. **Configure the Plugin:** Open your Anki personal configuration file and add the following information:

```json
{
  "beeminder_username": "user123",
  "beeminder_personal_auth_token": "abcdefghijklmnopqrstuvwxyz1234567890"
}
```

Replace `"user123"` with your Beeminder username and `"abcdefghijklmnopqrstuvwxyz1234567890"` with your Beeminder personal authentication token. (You can find this token under "Account Settings" -> "Apps & API".) This information is crucial for securely connecting your Anki and Beeminder accounts.

4. **Manual Sync:** To ensure everything is set up correctly, navigate to the "Tools" menu in Anki and select "Anki Zero Manual Sync." This action will initiate a synchronization of your Anki due data points to your specified Beeminder goal. You can use this feature to verify that the plugin is working as intended.

## Stay On Track with Ease

The Anki to Beeminder Sync Plugin streamlines your learning journey by seamlessly integrating your Anki flashcard review schedule with your Beeminder goals. This synchronization empowers you to maintain a consistent and effective learning routine, ensuring that you make steady progress toward your educational objectives.

Never worry about falling behind in your studies again. Take advantage of the Anki to Beeminder Sync Plugin and experience the benefits of a well-structured, goal-driven approach to learning.

Start using the plugin today and make your learning experience more organized, efficient, and rewarding!

For any questions, support, or feedback, please contact us at support@anki-beeminder-sync.com.

---

*Disclaimer: This plugin is developed independently and is not affiliated with Anki or Beeminder. Use at your own discretion. 

The source code, however, is open to the public, and you can check yourself to make sure I'm not doing anything nasty 😉
