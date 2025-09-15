import google.generativeai as genai
import yaml, os, json, re

# Load Gemini API key from environment or config.yaml
CONFIG_PATH = "config.yaml"

api_key = os.getenv("GEMINI_API_KEY")
if not api_key and os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH) as file:
        data = yaml.safe_load(file)
        api_key = data.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No Gemini API key found in environment or config.yaml!")


genai.configure(api_key=api_key)


def clean_json(text: str) -> str:
    """
    Cleans Gemini's output so it can be parsed as JSON.
    - Extracts only { ... }
    - Removes trailing commas
    """
    # Extract only JSON block
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("❌ No JSON object found in response")
    text = text[start:end+1]

    # Remove trailing commas before } or ]
    text = re.sub(r",\s*([}\]])", r"\1", text)

    return text



def ats_extractor(resume_data):
    prompt = """
    You are an AI bot designed to parse resumes and extract comprehensive information and Summarize it.
    Extract the following details and return ONLY valid JSON (no explanations, no text outside JSON):
    
    {
      "personal_info": {
        "full_name": "",
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": "",
        "github": "",
        "portfolio": "",
        "summary": ""
      },
      "education": [
        {
          "degree": "",
          "institution": "",
          "year": "",
          "gpa": "",
          "location": ""
        }
      ],
      "experience": [
        {
          "position": "",
          "company": "",
          "duration": "",
          "location": "",
          "responsibilities": [],
          "achievements": []
        }
      ],
      "projects": [
        {
          "name": "",
          "description": "",
          "technologies": [],
          "duration": "",
          "key_features": []
        }
      ],
      "technical_skills": {
        "programming_languages": [],
        "frameworks": [],
        "databases": [],
        "tools": [],
        "cloud_platforms": []
      },
      "soft_skills": [],
      "certifications": [
        {
          "name": "",
          "issuer": "",
          "year": ""
        }
      ],
      "languages": [
        {
          "language": "",
          "proficiency": ""
        }
      ]
    }
    Instructions:
    - Fill all applicable fields from the resume.  
    - If information is not available, leave the field as an empty string "".  
    - Use arrays where multiple entries exist (e.g., skills, experiences, projects, education).  
    - Keep the output very concise so a user can read everything in 60–90 seconds. Avoid long descriptions.  
    - For Experiences → Responsibilities: summarize into max 2 short bullet points each.  
    - For Projects → Key Features/Contributions: summarize into max 2 short bullet points each.  
    """

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(
        [prompt, resume_data],
        generation_config={
            "temperature": 0.0,
            "max_output_tokens": 5000
        }
    )

    # Attempt to get text parts robustly
    def _extract_response_text(response):
        # Try .text accessor first
        try:
            return response.text.strip()
        except Exception:
            # Fallback: try to join all candidate content parts
            try:
                texts = []
                for candidate in response.candidates:
                    for part in getattr(candidate, 'content', {}).get('parts', []):
                        if hasattr(part, 'text'):
                            texts.append(part.text)
                return "\n".join(texts).strip()
            except Exception:
                return ""

    raw_output = _extract_response_text(response)
    if not raw_output:
        raise ValueError(f"❌ No valid response from Gemini API. Check prompt, API quota, or model output restrictions.")


    # ✅ Clean and parse safely
    try:
        cleaned = clean_json(raw_output)
        parsed = json.loads(cleaned)
    except Exception as e:
        print(f"❌ JSON Parsing Error: {e}")
        print(f"Raw Output: {raw_output}")
        # Return a default structure if parsing fails
        return {
            "error": "Failed to parse resume",
            "raw_output": raw_output,
            "personal_info": {"full_name": "Unable to extract", "email": ""},
            "education": [], "experience": [], "projects": [],
            "technical_skills": {}, "soft_skills": [], "certifications": [], "languages": []
        }

    return parsed  # return dict directly

