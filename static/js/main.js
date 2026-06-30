document.addEventListener("DOMContentLoaded", function () {
    const atlasPreview = document.getElementById("atlasPreview");
    const atlasTabs = document.querySelectorAll(".atlas-v2-sidebar a");

    if (!atlasPreview || !atlasTabs.length) {
        return;
    }

    const content = {
        dashboard: `
            <div class="preview-toolbar">
                <span>Dashboard</span>
                <span>Study Flow</span>
                <span>AI Guided</span>
            </div>

            <div class="atlas-screen dashboard-screen-v3">
                <div class="atlas-screen-header">
                    <span>Dashboard</span>
                    <h3>Your study workspace, organized by AI.</h3>
                </div>

                <div class="dashboard-v3-layout">
                    <div class="dashboard-v3-focus">
                        <span>Study Flow</span>
                        <strong>Notes → Practice → Mock → Review</strong>
                        <p>Move through one structured preparation path instead of jumping between disconnected tools.</p>
                    </div>

                    <div class="dashboard-v3-card">
                        <span>Next Step</span>
                        <strong>Generate Notes</strong>
                    </div>

                    <div class="dashboard-v3-card">
                        <span>Practice</span>
                        <strong>Question Bank</strong>
                    </div>

                    <div class="dashboard-v3-card">
                        <span>Review</span>
                        <strong>Weak Areas</strong>
                    </div>

                    <div class="dashboard-v3-card">
                        <span>Status</span>
                        <strong>On Track</strong>
                    </div>
                </div>
            </div>
        `,

        notes: `
            <div class="preview-toolbar">
                <span>AI Notes</span>
                <span>Revision-ready</span>
                <span>PDF Export</span>
            </div>

            <div class="atlas-screen notes-screen-v3">
                <div class="atlas-screen-header">
                    <span>AI Notes</span>
                    <h3>Structured notes that feel ready to revise.</h3>
                </div>

                <div class="notes-v3-layout">
                    <div class="notes-v3-main">
                        <div class="notes-doc-header">
                            <span>Chapter Notes</span>
                            <h4>Sample Chapter</h4>
                        </div>

                        <div class="notes-doc-block">
                            <strong>Summary</strong>
                            <p>A clean overview of the chapter in simple, revision-friendly language.</p>
                        </div>

                        <div class="notes-doc-block">
                            <strong>Key Concepts</strong>
                            <p>Important ideas organized into short, easy-to-scan sections.</p>
                        </div>

                        <div class="notes-doc-block">
                            <strong>Formula Sheet</strong>
                            <p>Important formulas collected in one place for quick revision.</p>
                        </div>
                    </div>

                    <div class="notes-v3-side">
                        <div>
                            <span>Includes</span>
                            <strong>Common Mistakes</strong>
                        </div>

                        <div>
                            <span>Revision</span>
                            <strong>Quick Points</strong>
                        </div>

                        <div>
                            <span>Export</span>
                            <strong>PDF Ready</strong>
                        </div>
                    </div>
                </div>
            </div>
        `,

        questions: `
            <div class="preview-toolbar">
                <span>Question Bank</span>
                <span>Topic-wise Practice</span>
                <span>Difficulty Levels</span>
            </div>

            <div class="atlas-screen questions-screen-v3">
                <div class="atlas-screen-header">
                    <span>Question Bank</span>
                    <h3>Practice with questions matched to your preparation level.</h3>
                </div>

                <div class="questions-v3-layout">
                    <div class="questions-v3-card selected">
                        <span>Easy</span>
                        <strong>Concept Check</strong>
                        <p>Build confidence with basic understanding questions.</p>
                    </div>

                    <div class="questions-v3-card">
                        <span>Medium</span>
                        <strong>Application</strong>
                        <p>Apply concepts across slightly deeper practice prompts.</p>
                    </div>

                    <div class="questions-v3-card">
                        <span>Hard</span>
                        <strong>Exam Level</strong>
                        <p>Prepare for challenging questions and mixed concepts.</p>
                    </div>
                </div>

                <div class="questions-v3-footer">
                    <span>10 questions ready</span>
                    <button>Start Practice</button>
                </div>
            </div>
        `,

        mocks: `
            <div class="preview-toolbar">
                <span>Mock Tests</span>
                <span>Exam-style Practice</span>
                <span>Review Enabled</span>
            </div>

            <div class="atlas-screen mocks-screen-v3">
                <div class="atlas-screen-header">
                    <span>Mock Test</span>
                    <h3>Practice under focused test conditions.</h3>
                </div>

                <div class="mock-v3-layout">
                    <div class="mock-v3-question">
                        <span>Question 4 / 20</span>
                        <h4>Which method is best suited to solve this equation?</h4>

                        <div class="mock-option">Factorisation</div>
                        <div class="mock-option active">Completing the square</div>
                        <div class="mock-option">Quadratic formula</div>
                        <div class="mock-option">Graph method</div>
                    </div>

                    <div class="mock-v3-side">
                        <div>
                            <span>Time</span>
                            <strong>45 min</strong>
                        </div>

                        <div>
                            <span>Difficulty</span>
                            <strong>Medium</strong>
                        </div>

                        <div>
                            <span>Review</span>
                            <strong>Enabled</strong>
                        </div>
                    </div>
                </div>
            </div>
        `,

        analytics: `
            <div class="preview-toolbar">
                <span>Analytics</span>
                <span>Weak Areas</span>
                <span>Study Direction</span>
            </div>

            <div class="atlas-screen analytics-screen-v3">
                <div class="atlas-screen-header">
                    <span>Performance Insights</span>
                    <h3>Know what to improve before the next study session.</h3>
                </div>

                <div class="analytics-v3-layout">
                    <div class="analytics-score-card">
                        <span>Readiness Score</span>
                        <strong>82%</strong>
                        <p>Good progress. One weak area needs attention.</p>
                    </div>

                    <div class="analytics-v3-bars">
                        <div>
                            <span>Concept Clarity</span>
                            <strong><em style="width: 82%"></em></strong>
                        </div>

                        <div>
                            <span>Practice Accuracy</span>
                            <strong><em style="width: 68%"></em></strong>
                        </div>

                        <div>
                            <span>Mock Readiness</span>
                            <strong><em style="width: 74%"></em></strong>
                        </div>
                    </div>

                    <div class="analytics-recommendation-card">
                        <span>AI Recommendation</span>
                        <strong>Revise Algebra before your next mock.</strong>
                    </div>
                </div>
            </div>
        `,

        coach: `
            <div class="preview-toolbar">
                <span>Study Coach</span>
                <span>AI Guidance</span>
                <span>Next Steps</span>
            </div>

            <div class="atlas-screen coach-screen-v3">
                <div class="atlas-screen-header">
                    <span>AI Study Coach</span>
                    <h3>A calm study plan after every session.</h3>
                </div>

                <div class="coach-chat">
                    <div class="coach-message ai">
                        <span>Genelis Coach</span>
                        <p>You understood most concepts well. Focus next on the topic where mistakes repeated.</p>
                    </div>

                    <div class="coach-task-list">
                        <div>Revise weak concepts</div>
                        <div>Attempt a 15-minute mock</div>
                        <div>Review incorrect answers</div>
                        <div>Follow tomorrow’s plan</div>
                    </div>
                </div>
            </div>
        `
    };

    atlasTabs.forEach(function (tab) {
        tab.addEventListener("click", function () {
            const selected = tab.getAttribute("data-atlas-tab");

            atlasTabs.forEach(function (item) {
                item.classList.remove("active");
            });

            tab.classList.add("active");

            if (content[selected]) {
                atlasPreview.style.opacity = "0";

                setTimeout(function () {
                    atlasPreview.innerHTML = content[selected];
                    atlasPreview.style.opacity = "1";
                }, 160);
            }
        });
    });
});