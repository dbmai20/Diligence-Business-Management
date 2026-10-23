<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>DBM AI Calling Agent</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        background: #f4f7fb;
        color: #1f2937;
      }
      .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 24px;
      }
      .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 24px;
      }
      .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
      }
      .panel {
        background: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
      }
      .card {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 14px;
        margin-bottom: 12px;
      }
      form {
        display: grid;
        gap: 10px;
      }
      input, select, textarea, button {
        padding: 10px 12px;
        border-radius: 8px;
        border: 1px solid #d1d5db;
        font-size: 14px;
      }
      button {
        background: #2563eb;
        color: white;
        border: none;
        cursor: pointer;
      }
      h2, h3 {
        margin-top: 0;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <div>
          <h1>DBM AI Calling Agent</h1>
          <p>Telemarketing operations dashboard</p>
        </div>
      </div>

      <div class="grid">
        <div class="panel">
          <h2>Create Campaign</h2>
          <form id="campaignForm">
            <input name="name" placeholder="Campaign name" required />
            <input name="objective" placeholder="Campaign objective" required />
            <textarea name="script" placeholder="Sales script" rows="4" required></textarea>
            <input name="target_audience" placeholder="Target audience" value="SMB" />
            <input name="timezone" placeholder="Timezone" value="UTC" />
            <button type="submit">Create Campaign</button>
          </form>
        </div>

        <div class="panel">
          <h2>Add Lead</h2>
          <form id="leadForm">
            <input name="name" placeholder="Lead name" required />
            <input name="phone" placeholder="Phone number" required />
            <input name="company" placeholder="Company" />
            <select name="source">
              <option value="manual">Manual</option>
              <option value="list">Lead list</option>
              <option value="web">Website</option>
            </select>
            <select name="priority">
              <option value="normal">Normal</option>
              <option value="high">High</option>
              <option value="vip">VIP</option>
            </select>
            <button type="submit">Add Lead</button>
          </form>
        </div>

        <div class="panel">
          <h2>Queue Call</h2>
          <form id="callForm">
            <input name="campaign_id" placeholder="Campaign ID" required />
            <input name="agent_id" placeholder="Agent ID" value="agent_default" required />
            <input name="lead_id" placeholder="Lead ID" required />
            <select name="call_type">
              <option value="outbound">Outbound</option>
              <option value="follow_up">Follow Up</option>
              <option value="survey">Survey</option>
            </select>
            <textarea name="notes" rows="3" placeholder="Call notes"></textarea>
            <button type="submit">Queue Call</button>
          </form>
        </div>
      </div>

      <div class="grid" style="margin-top: 24px;">
        <div class="panel">
          <h2>Campaigns</h2>
          <div id="campaigns"></div>
        </div>
        <div class="panel">
          <h2>Leads</h2>
          <div id="leads"></div>
        </div>
        <div class="panel">
          <h2>Agents</h2>
          <div id="agents"></div>
        </div>
        <div class="panel">
          <h2>Calls</h2>
          <div id="calls"></div>
        </div>
      </div>
    </div>

    <script src="/static/app.js"></script>
  </body>
</html>
