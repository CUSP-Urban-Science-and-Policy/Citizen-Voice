SELECT ans.*, res.*, mapv.*, sur.*, que.*
FROM public.apiapp_answer AS ans,
	public.apiapp_response as res,
	public.apiapp_mapview as mapv,
	public.apiapp_survey as sur,
	public.apiapp_question as que
WHERE ans.response_id = res.response_id 
	AND res.survey_id = sur.id
	AND ans.mapview_id = mapv.id
	AND que.survey_id = sur.id
ORDER BY ans.id ASC
