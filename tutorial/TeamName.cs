using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Photon.Pun;
using UnityEngine.Networking;

[System.Serializable]
public class Team
{
    public string team_name;
    public string start_date;
    public string end_date;
    public static Team CreateFromJSON(string jsonString)
    {
        //Debug.Log(jsonString);
        return JsonUtility.FromJson<Teams>(jsonString);
    }
}

public class TeamName : MonoBehaviourPun
{
    void Start() {
        StartCoroutine(GetText());
        }
 
    IEnumerator GetText() {
        UnityWebRequest www = UnityWebRequest.Get("http://localhost:8000/teamDetails");
        yield return www.SendWebRequest();
 
        if(www.isNetworkError || www.isHttpError) {
            Debug.Log(www.error);
        }
        else {
            // Show results as text
            
            //Debug.Log(www.downloadHandler.text);
            string jsonString = www.downloadHandler.text;            //bug.Log(teams.teams);
            
for(int i = 0 ; i < 10; i++)
            {
                string teamJsonString = JsonHelper.GetJsonObject(jsonString,""+i);
                Team team = Team.CreateFromJson(teamJsonString);
                Debug.Log(team.team_name);
            }
            // Or retrieve results as binary data
            byte[] results = www.downloadHandler.data;
        }
    }
    // public void PlaceUserInfo(string name, string email)
    // {
    //     string PlayerNickname = name;
    //     PhotonNetwork.NickName = PlayerNickname;
    //     PlayerPrefs.SetString("PlayerName", PlayerNickname);
    //     PlayerPrefs.SetString("PlayerEmail", email);
    //     //Debug.Log(nameInputField.text);
    // }
}
