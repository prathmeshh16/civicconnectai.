Project Specification Sheet

Project Name: CivicConnect AI

Tagline: Verify Before You Trust.

1. Project Overview

CivicConnect AI is a website that helps people check whether the information they see online is real or misleading. Nowadays, fake news, edited images, AI-generated videos, and fake audio are spreading quickly on social media. Many people share this content without knowing whether it is genuine.

Our idea is to build a platform where users can paste text or upload images, videos, and audio files to check them. The system will analyse the content using AI and compare available information with trusted websites and reliable sources. It will then show a report explaining the result in simple language.

2. Problem Statement

Fake news and misleading information have become common on the internet. It is difficult for normal users to identify whether a news report, image, video, or audio recording is genuine or has been changed using editing tools or AI.

People usually have to visit different websites to verify information, which takes time and can be confusing. There is a need for one simple platform that can help users check suspicious content and understand whether it can be trusted.

CivicConnect AI aims to solve this problem by providing an easy way to verify online information using AI-based analysis and trusted sources.

3. Main Features

1. Text Verification

- Users can paste news, messages, or online claims.
- The system checks the claim against available trusted sources.
- It shows whether the claim is supported, contradicted, misleading, or unverified.

2. Image Verification

- Users can upload an image.
- The system checks available image details and signs of possible editing or AI generation.
- It displays the analysis result.

3. Video Verification

- Users can upload a video.
- The system can analyse selected video frames.
- It checks for possible signs of manipulation or AI-generated content.

4. Audio Verification

- Users can upload an audio file.
- The system can convert speech into text where supported.
- It checks the transcript and available audio signals for possible manipulation.

5. Trusted Source Checking

- Compare claims with reliable websites and official sources.
- Show the source name and link.
- Display the date of the available information.

6. Verification Report

- Show the final result in a simple format.
- Display the reason behind the result.
- Include supporting links and available evidence.
- Show a confidence level where the analysis supports one.

7. History

- Save previous verification results.
- Allow users to view their earlier reports.

4. Result Categories

The system should use these result labels:

- Supported: Reliable sources support the claim.
- Contradicted: Reliable sources provide evidence against the claim.
- Misleading: The information is missing important context or may create a wrong impression.
- Unverified: There is not enough reliable information to confirm the claim.

For image, video, and audio checks, show a separate result for possible AI generation or manipulation. Do not treat an AI detector score as definite proof.

5. Website Pages

1. Home Page: Project introduction and a button to start verification.
2. Verification Page: Options to check text, images, videos, and audio.
3. Result Page: Shows the analysis and supporting information.
4. History Page: Displays previous verification reports.
5. About Page: Explains the project and its purpose.

6. Technology to Use

Frontend:

- HTML
- CSS
- JavaScript
- Bootstrap

Backend:

- Python
- Flask

Database:

- SQLite for the initial version.

AI and Verification:

- AI API for text analysis.
- Image analysis API or model.
- Speech-to-text service for audio.
- Video frame extraction and analysis.
- Trusted website or fact-checking source integration.

Use APIs only when available and properly configured. Keep the code ready for adding more AI services later.

7. Website Design

- Create a modern and professional-looking website.
- Use dark blue, white, and light cyan as the main colours.
- Make the website responsive for mobile, tablet, and desktop.
- Keep the navigation simple.
- Use separate upload sections for text, images, videos, and audio.
- Show verification results using clear labels and simple cards.
- Make the website easy for anyone to understand.

8. How the System Should Work

1. User opens the CivicConnect AI website.
2. User selects what they want to verify.
3. User pastes text or uploads a file.
4. The system analyses the submitted content.
5. It checks available information against trusted sources.
6. The system generates a report.
7. User can view the result and save it in history.

9. Important Instructions

- Do not show random or fake verification results.
- Do not claim that AI detection is always 100% accurate.
- Show "Unable to Verify" when there is not enough evidence.
- Provide links for sources used in verification.
- Clearly separate claim verification from AI-media detection.
- Do not claim to identify the original creator or spread of content unless reliable source or sharing-history data is available.
- Keep user-uploaded files and information secure.
- If an API is not connected, clearly show that the feature is unavailable instead of showing a fake result.

10. Expected Output

Build a working website where users can submit online claims, images, videos, and audio for verification. The website should analyse the content, check available trusted sources, and display a simple report that helps users understand whether the information can be trusted.

Final Goal: Make it easier for people to identify misleading information and think before sharing anything online.