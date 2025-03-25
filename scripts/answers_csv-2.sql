SELECT DISTINCT 
	-- sur.id as survey_id, que.*, ans.id as answer_id, 
	res.response_id, res.survey_id,
	que.text as question, 
	ans.id, ans.created, ans.updated, ans.body,
	mapv.*
FROM 
	public.apiapp_answer AS ans,
	public.apiapp_response as res,
	public.apiapp_mapview as mapv,
	-- public.apiapp_survey as sur,
	public.apiapp_question as que
WHERE  res.survey_id=3 and ans.question_id = que.id 
	-- AND
	-- ans.response_id = res.response_id 
	-- -- AND 
	-- -- 
	-- AND res.survey_id = sur.id
	-- AND ans.mapview_id = mapv.id
	-- AND que.survey_id = sur.id
	-- and ans.id = 46
ORDER BY res.response_id ASC
